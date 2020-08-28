const Firestore = require('@google-cloud/firestore');
const functions = require('firebase-functions');
const PROJECTID = 'stash-share';
const COLLECTION = 'patches';
const firestore = new Firestore({
    projectId: PROJECTID,
    timestampsInSnapshots: true,
})


exports.sendPatch = functions.https.onRequest((request, response) => {
    return firestore.collection(COLLECTION).where('name', '==', request.body.name)
        .get()
        .then(querySnapshot => {
            querySnapshot.docs.forEach(doca => {
                doca.ref.delete()
            })
            return firestore.collection(COLLECTION).add(request.body)
                .then(doc => {
                    return response.status(200).send(doc.id);
                }).catch(err => {
                    functions.logger.info(err);
                    return response.status(404).send({ error: 'unable to store', err });
                });
        }).catch(err => {
            functions.logger.info(err);
            return response.status(404).send({ error: 'unable to delete', err });
        });
});

exports.getPatch = functions.https.onRequest((request, response) => {
    functions.logger.info(request.query.name);
    return firestore.collection(COLLECTION).where('name', '==', request.query.name)
        .get()
        .then(querySnapshot => {
            return querySnapshot.docs.forEach(doc => {
                return response.status(200).send(doc.data());
            })
        }).catch(err => {
            functions.logger.info(err);
            return response.status(404).send({ error: 'unable to get', err });
        });
});