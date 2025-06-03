import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('C:\\Users\\njmar\\sidney_crosby\\sidney-crosby-6dddd32d679f.json')
firebase_admin.initialize_app(cred)

# Alternatively, you can initialize the app without a service account.
# Application Default credentials are automatically created.
app = firebase_admin.initialize_app()

db = firestore.client()

# Add data
# eg
doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

doc_ref = db.collection("users").document("aturing")
doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

# Read data
users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

# Secure data
# If you're using the web, Android, or Apple platforms SDK, use Firebase Authentication and Cloud Firestore Security Rules to secure your data in Cloud Firestore.
# Here are some basic rule sets you can use to get started. You can modify your security rules in the Rules tab of the console.
