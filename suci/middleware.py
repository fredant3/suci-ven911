import logging
from user_agents import parse


class CaptureIPAndDeviceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        user_agent = request.META.get("HTTP_USER_AGENT", "unknown")
        user_agent_parsed = parse(user_agent)

        ip = self.get_client_ip(request)
        device_type = self.get_device_type(user_agent_parsed)
        device_name = self.get_device(user_agent_parsed)
        os = self.get_os(user_agent_parsed)
        browser = self.get_browser(user_agent_parsed)

        self.logger.info(
            f"IP: {ip}, Conectado desde: {device_type}, Dispositivo: {device_name}, Sistema Operativo: {os}, Navegador: {browser}"
        )

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def get_device_type(self, user_agent):
        if user_agent.is_mobile:
            return "Mobile"
        elif user_agent.is_tablet:
            return "Tablet"
        elif user_agent.is_pc:
            return "PC"
        else:
            return "Other"

    def get_device(self, user_agent):
        return f"{user_agent.device.family} {user_agent.device.brand} {user_agent.device.model}"

    def get_os(self, user_agent):
        return f"{user_agent.os.family} {user_agent.os.version_string}"

    def get_browser(self, user_agent):
        return f"{user_agent.browser.family} {user_agent.browser.version_string}"
