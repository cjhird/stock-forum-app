from .common import ThreadSerializer
from comments.serializers.populated import PopulatedCommentSerializer
from jwt_auth.serializers.common import UserSerializer



class PopulatedThreadSerializer(ThreadSerializer):
    comments = PopulatedCommentSerializer(many=True)
    owner = UserSerializer()
