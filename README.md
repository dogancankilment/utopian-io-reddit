# utopian-io-reddit
Django project for analyzing the utopian-io entries "reddit.com/r/utopianio" on reddit.
For a long time, every time I logged into utopian, on the right side, I saw the reddit script and the link. I thought that I should analyze the shares made on this link.

The filters I think for the moment.
- entries count
- entry title
- entry author
- entry author_detail full url
- entry link
- entry updated date

Futures
- How are posts shared?
- To be able to pass the created shares over specific filters and create analysis visuals and graphs. (Maybe author's nationality, tags, content types.

Able to be extended with your ideas or suggestions.

Technology Stack
- Minimum Django 1.4.8
- Python 2.7.x
- Feedparser (from Python)
- Apache2 Web Server
- css3 / html5 / bootstrap static files

Apache2 config and wsgi files finally done on cloud droplet.
This project live at;
http://utopian-io-reddit.duckdns.org/

Features:
# v1.1 Reddit Analysis Auth
- Authentication and user profile structure added.
- Created queries are being recorded.

Using duckdns.org subdomain free domain service. If you interest my project, you can do donate for hosting and domain costs.
Thanks for all.
