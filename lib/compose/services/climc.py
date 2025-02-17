from lib.compose.object import ServiceDataVolume
from lib.compose.services import ClusterCommonService


class ClimcService(ClusterCommonService):

    def __init__(self, version, keystone):
        super().__init__("climc", version, keystone_svc=keystone)
        self.depend_on_completed(keystone.get_post_init_service())

    def get_command(self):
        return ["tail", "-f", "/dev/null"]

    def get_config_path(self):
        return self.YUNION_ETC_PATH + "rcadmin"

    def _get_init_service(self):
        svc = super()._get_init_service()
        svc.add_environment({
            "CLIMC_DEFAULT_USER": "admin",
            "CLIMC_DEFAULT_USER_PASSWORD": "admin@123",
        })
        return svc

    def _get_post_init_service(self):
        return None
