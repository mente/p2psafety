from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import Unauthorized


class CreateFreeDjangoAuthorization(DjangoAuthorization):
    """
    Allows anyone to make create requests.
    Also, requires read permissions.
    """
    def create_detail(self, object_list, bundle):
        return True

    def read_list(self, object_list, bundle):
        klass = self.base_checks(bundle.request, bundle.obj.__class__)

        permission = '%s.view_%s' % (klass._meta.app_label, klass._meta.module_name)
        if not bundle.request.user.has_perm(permission):
            raise Unauthorized('You are not allowed to access that resource.')

        return object_list

