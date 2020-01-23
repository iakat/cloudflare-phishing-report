import requests



class Report:
    def __init__(self, url, submitter, justification, session=None):
        self.url = url
        self.form = 'https://www.cloudflare.com/api/v2/abuse/phishing'

        self.submitter = submitter['name']
        self.submitter_email = submitter['email']
        self.submitter_company = submitter['company']
        self.justification = justification

        self.session = session or requests.Session()

    @property
    def _token(self):
        R = self.session.post(self.form)
        print('token', R.json()['response']['security_token'])
        return R.json()['response']['security_token']

    def report(self):
        token = self._token

        R = self.session.post(
            self.form,
            data={
                'act': 'abuse_phishing',
                'email': self.submitter_email,
                'email2': self.submitter_email,
                'title': '',
                'name': self.submitter,
                'company': self.submitter_company,
                'justification': self.justification,
                'agree': '1',
                'urls': self.url,
                'security_token': token,
                'host_notification': 'send',
                'owner_notification': 'send',
            })
        print('report', R.text)
        return R
