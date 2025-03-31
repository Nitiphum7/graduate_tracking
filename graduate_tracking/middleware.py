import time
import logging
from django.utils import timezone

logger = logging.getLogger('access_log')

class AccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        # Calculate response time
        duration = time.time() - start_time
        
        # Log access details
        log_data = {
            'timestamp': timezone.now().isoformat(),
            'user': request.user.username if request.user.is_authenticated else 'anonymous',
            'method': request.method,
            'path': request.path,
            'status': response.status_code,
            'duration': duration,
            'ip': self.get_client_ip(request)
        }
        
        logger.info(f"ACCESS: {log_data}")
        
        return response
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
