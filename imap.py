import email
import imaplib
from email.parser import BytesParser

# TODO: Look into parse .eml files instead

tvl_host = 'mail.tvlitho.com'
tvl_user = 'doug@tvlitho.com'
tvl_pass = '29phillipPi*'


def connect_to_host(tvl_host, tvl_user, tvl_pass):
    """
    Connect to email host and login.

    Args:
        tvl_host (str): name of host
        tvl_user (str): username
        tvl_pass (str): password

    Returns:
        obj: imaplib.IMAP4 object
    """
    while True:
        #  Connect and login to host
        imap = imaplib.IMAP4(tvl_host)
        r, d = imap.login(tvl_user, tvl_pass)
        assert r == 'OK', 'login failed'

        #  Continue connection attempts
        try:
            return imap
            break
        except imap.abort as e:
            print(e)
            continue


def parse_mail(imap):
    """
    Enter user inbox and search emails using given parameter(s).

    Args:
        imap (obj): imaplib.IMAP4 object

    Returns:
        str: email body
    """
    imap.select('INBOX')  # Enter inbox

    # TODO: Search for ProTeam specific emails using input
    status, msg_count = imap.search(None, 'FROM "Debi"')

    for id in msg_count[0].split()[-1:]:
        res, msg = imap.fetch(id, "(RFC822)")
        msg = email.message_from_bytes(msg[0][1])
        print(f'''
        =======================================================================
        {msg['from']}
        {msg['to']}
        {msg['subject']}
        =======================================================================
        ''')  # TODO: Remove once finished

        # Prints email body
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    obj = part.get_payload(decode=True)
                    parser = BytesParser()
                    body = parser.parsebytes(obj)
                    print(obj)  # TODO: Parse better?

    return body


if __name__ == '__main__':
    imap = connect_to_host(tvl_host, tvl_user, tvl_pass)
    body = parse_mail(imap)
    print(body)

    # Logout of host
    imap.logout()
