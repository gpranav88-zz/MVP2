from django.http import HttpResponse, JsonResponse
import json
import difflib

def index(request):
    return HttpResponse("1MG MegaMind")


def run_rule():
    pass


def check_duplicate_email(request):
    new_email = request.GET.get('email', '').lower()
    with open('./phoenix/data/email_cluster.json') as data_file:
        cluster_data = json.load(data_file)
    clusters = cluster_data['clusters']
    high_risk_emails = []
    for cluster in clusters:
        if cluster['size'] > 4:
            high_risk_emails.append(cluster['value'])
    for email in high_risk_emails:
        seq = difflib.SequenceMatcher(a=new_email, b=email.lower())
        if seq.ratio() > 0.8:
            print(email, seq.ratio())
            return JsonResponse({'email': email, 'score': seq.ratio(), 'match': True})
    return JsonResponse({'match': False})
