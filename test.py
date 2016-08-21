from wallet.models import Pass, Barcode, StoreCard

cardInfo = StoreCard() 
cardInfo.addPrimaryField('name', 'John Doe', 'Name')

organizationName = 'Phils Pass Generator' 
passTypeIdentifier = 'pass.de.mobilcom.25jahre' 
teamIdentifier = 'N642X794C7'

passfile = Pass(cardInfo, passTypeIdentifier=passTypeIdentifier, organizationName=organizationName, teamIdentifier=teamIdentifier)
passfile.serialNumber = '1234567'
passfile.barcode = Barcode(message = 'Barcode message')

# Including the icon and logo is necessary for the passbook to be valid. 
passfile.addFile('icon.png', open('images/icon.png', 'r')) 
passfile.addFile('logo.png', open('images/logo.png', 'r')) 
passfile.create('certificate.pem', 'key.pem', 'wwdr.pem', 'test', 'passes/test.pkpass') # Create and output the Passbook file (.pkpass)
