from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

milo = Pet(name='Milo', species='cat', photo_url='https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcT2fOqem4ruHAuY3m_EZDY5tkG3j2lAadjPhT4O80P7SPj_XLRpjWFFcXt43BlruXVNyECd55RY1bDOIX0', age='1', notes='very energetic', available=True)
toes = Pet(name='Toes', species='cat', photo_url='https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg', age='1', notes='very sweet', available=True)
sonya = Pet(name='Sonya', species='cat', photo_url='https://npr.brightspotcdn.com/8f/67/3e8a293a4f60adda1ce9743da20a/grey-tabby-cat-rosebud-03.jpg', age='1', notes='not social', available=False)

db.session.add(milo)
db.session.add(sonya)
db.session.add(toes)

db.session.commit()