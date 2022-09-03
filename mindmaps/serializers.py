from wsgiref import validate
from rest_framework import serializers
from .models import Branch, BranchLine, Mindmap

class BranchLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchLine
        fields = ['sort_number', 'content', 'branch', 'id']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['sort_number', 'id', 'title', 'mindmap', 'content']

    sort_number = serializers.IntegerField()
    content = BranchLineSerializer(many=True, read_only=True, source='content_line')


class SimpleBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['sort_number', 'id', 'title', 'mindmap', 'content']

    mindmap = serializers.PrimaryKeyRelatedField(read_only=True)
    sort_number = serializers.IntegerField()
    content = BranchLineSerializer(many=True, read_only=True, source='content_line')

class MindmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mindmap
        fields = ['id', 'title', 'category', 'revisions', 'branches']

    branches = SimpleBranchSerializer(many=True, read_only=True)

class AddBranchLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchLine
        fields = ['content', 'id']

class AddBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'title', 'content']
    content = AddBranchLineSerializer(many=True, source='content_line')

class AddMindmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mindmap
        fields = ['id', 'title', 'category', 'revisions', 'branches']

    branches = AddBranchSerializer(many=True)

    def create(self, validated_data):
        branches = validated_data.pop('branches')
        mindmap  = Mindmap(**validated_data)
        mindmap.save()

        branch_lines = []
        for idx, branch in enumerate(branches):
            b = Branch(title=branch['title'], mindmap=mindmap, sort_number=idx+1)
            b.save()
            for j, line in enumerate(branch['content_line']):
                b_line = BranchLine(content=line['content'], branch=b, sort_number=j+1)
                branch_lines.append(b_line)        
        BranchLine.objects.bulk_create(branch_lines)

        return mindmap

class UpdateBranchLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchLine
        fields = ['content', 'id']
    id = serializers.IntegerField(read_only=False, required=False)


class UpdateBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'title', 'content']
    id = serializers.IntegerField(read_only=False, required=False)
    content = UpdateBranchLineSerializer(many=True, source='content_line')
        
class UpdateMindmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mindmap
        fields = ['id', 'title', 'category', 'revisions', 'branches']

    branches = UpdateBranchSerializer(many=True)

    def update(self, instance, validated_data):
        branches = validated_data.pop('branches')
        instance.title = validated_data['title']
        instance.category = validated_data['category']
        instance.revisions = validated_data['revisions']
        instance.save()

        def update_branch(branch, idx):
            b = Branch.objects.get(pk=branch['id'])
            b.title = branch['title']
            b.sort_number = idx+1
            b.save()
            return b
        def create_branch(branch, idx):
            b = Branch(title=branch['title'], mindmap=instance, sort_number=idx+1)
            b.save()
            return b
        def update_branchline(line, branch, idx):
            BranchLine.objects.filter(pk=line['id']).update(content=line['content'], branch=branch, sort_number=idx+1)
        def create_branchline(line, branch, idx):
            BranchLine(content=line['content'], branch=branch, sort_number=idx+1).save()


        for idx, branch in enumerate(branches):
            if 'id' in branch.keys():
                b = update_branch(branch, idx)
                for j, line in enumerate(branch['content_line']):
                    if 'id' in line.keys():
                        update_branchline(line, b, j)
                    else:
                        create_branchline(line, b, j)
            else:
                b = create_branch(branch, idx)
                for j, line in enumerate(branch['content_line']):
                    create_branchline(line, b, j)

        return instance

    

class SimpleMindmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mindmap
        fields = ['id', 'title', 'category', 'revisions']

