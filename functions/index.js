const Firestore = require('@google-cloud/firestore');
const functions = require('firebase-functions');
const PROJECTID = 'stash-share';
const firestore = new Firestore({
    projectId: PROJECTID,
    timestampsInSnapshots: true,
  })  
// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.helloWorld = functions.https.onRequest((request, response) => {
  functions.logger.info("Hello logs!", {structuredData: true});
  response.send("Hello from Firebase!");
});


exports.sendPatch = functions.https.onRequest((request, response) => {
    functions.logger.info(request.body, {structuredData: true});
    return firestore.collection("patches")
      .add(request.body)
      .then(doc => {
        return response.status(200).send(doc);
      }).catch(err => {
        console.error(err);
        return response.status(404).send({ error: 'unable to store', err });
      });
  });
