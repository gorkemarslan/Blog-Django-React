from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):

    message = 'Only post owner can edit this post.'

    def has_object_permission(self, request, view, obj):
        # If HTTP methods is in ('GET', 'HEAD', 'OPTIONS'), then it is safe to be accessed to the content.
        if request.method in SAFE_METHODS:
            return True
        # Only author of a post can have write permissions
        return obj.author == request.user
