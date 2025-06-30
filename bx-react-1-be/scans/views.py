from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Scan
import json


@csrf_exempt
def get_scans(request):
    if request.method == 'GET':
        scans = Scan.objects.all()
        data = [{
            'id': scan.id,
            'filename': scan.filename,
            'patients': scan.get_patients(),
            'modalities': scan.get_modalities(),
            'warnings': scan.get_warnings(),
            'notes': scan.notes,
            'created_at': scan.created_at.isoformat(),
            'updated_at': scan.updated_at.isoformat()
        } for scan in scans]
        return JsonResponse({'error': False, 'data': data})
    return JsonResponse({'error': True, 'message': 'Method not allowed'}, status=405)


@csrf_exempt
def add_scan(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            scan = Scan.objects.create(
                filename=data.get('filename', ''),
                notes=data.get('notes', '')
            )

            # Set arrays using the helper methods
            scan.set_patients(data.get('patients', []))
            scan.set_modalities(data.get('modalities', []))
            scan.set_warnings(data.get('warnings', []))
            scan.save()

            return JsonResponse({
                'error': False,
                'message': 'Scan created successfully',
                'data': {
                    'id': scan.id,
                    'filename': scan.filename,
                    'patients': scan.get_patients(),
                    'modalities': scan.get_modalities(),
                    'warnings': scan.get_warnings(),
                    'notes': scan.notes,
                    'created_at': scan.created_at.isoformat(),
                    'updated_at': scan.updated_at.isoformat()
                }
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': True, 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': True, 'message': str(e)}, status=400)
    return JsonResponse({'error': True, 'message': 'Method not allowed'}, status=405)


@csrf_exempt
def edit_scan(request, scan_id):
    if request.method == 'PUT' or request.method == 'POST':
        try:
            scan = Scan.objects.get(id=scan_id)
            data = json.loads(request.body)

            # Update fields if they exist in the request
            if 'filename' in data:
                scan.filename = data['filename']
            if 'notes' in data:
                scan.notes = data['notes']
            if 'patients' in data:
                scan.set_patients(data['patients'])
            if 'modalities' in data:
                scan.set_modalities(data['modalities'])
            if 'warnings' in data:
                scan.set_warnings(data['warnings'])

            scan.save()

            return JsonResponse({
                'error': False,
                'message': 'Scan updated successfully',
                'data': {
                    'id': scan.id,
                    'filename': scan.filename,
                    'patients': scan.get_patients(),
                    'modalities': scan.get_modalities(),
                    'warnings': scan.get_warnings(),
                    'notes': scan.notes,
                    'created_at': scan.created_at.isoformat(),
                    'updated_at': scan.updated_at.isoformat()
                }
            })
        except Scan.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Scan not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': True, 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': True, 'message': str(e)}, status=400)
    return JsonResponse({'error': True, 'message': 'Method not allowed'}, status=405)


@csrf_exempt
def delete_scan(request, scan_id):
    if request.method == 'DELETE' or request.method == 'POST':
        try:
            scan = Scan.objects.get(id=scan_id)
            scan.delete()
            return JsonResponse({
                'error': False,
                'message': 'Scan deleted successfully'
            })
        except Scan.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Scan not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': True, 'message': str(e)}, status=400)
    return JsonResponse({'error': True, 'message': 'Method not allowed'}, status=405)