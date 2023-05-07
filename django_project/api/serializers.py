from rest_framework import serializers
from projects.models import Thumbnail, Project, Rate


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ("image_url",)


class ProjectSerializer(serializers.ModelSerializer):
    end_date = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", required=False)
    img_url = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()
    thumbnails = ThumbnailSerializer(many=True, write_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "details",
            "target_amount",
            "end_date",
            "category",
            "tags",
            "rate",
            "img_url",
            "thumbnails",
        )

    def get_img_url(self, obj):
        image_url = obj.get_img_url()
        if image_url:
            serializer = ThumbnailSerializer(image_url, many=True)
            return serializer.data
        return None

    def get_rate(self, obj):
        counts = {}
        for i in range(1, 6):
            cnt = Rate.objects.filter(project=obj, value=i).count()
            counts[i] = cnt
        num_1 = counts.get(1, 0)
        num_2 = counts.get(2, 0)
        num_3 = counts.get(3, 0)
        num_4 = counts.get(4, 0)
        num_5 = counts.get(5, 0)
        avg_rate = (num_5 * 5 + num_4 * 4 + num_3 * 3 + num_2 * 2 + num_1 * 1) / (
            float(num_5 + num_4 + num_3 + num_2 + num_1)
        )
        rate_data = {
            "num_1": num_1,
            "num_2": num_2,
            "num_3": num_3,
            "num_4": num_4,
            "num_5": num_5,
            "avg_rate": avg_rate,
        }
        return rate_data

    def create(self, validated_data):
        thumbnail_data = validated_data.pop("thumbnails")
        project = Project.objects.create(**validated_data)
        for data in thumbnail_data:
            Thumbnail.objects.create(project=project, **data)
        return project
