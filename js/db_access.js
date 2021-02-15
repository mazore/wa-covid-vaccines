// This is a read only key I promise
const dbConfig = {
    /* spell-checker: disable */
    apiKey: "AIzaSyB6n5x6YmOqBYNtZx8uiSsZNfKFLL8HTtk",
    authDomain: "covid-vaccines.firebaseapp.com",
    databaseURL: "https://covid-vaccines-default-rtdb.firebaseio.com",
    projectId: "covid-vaccines",
    storageBucket: "covid-vaccines.appspot.com",
    messagingSenderId: "805952005322",
    appId: "1:805952005322:web:b13f8f2cd47a36dcc58033",
    measurementId: "G-HDWG7J9KPB"
    /* spell-checker: enable */
};
firebase.initializeApp(dbConfig);
const database = firebase.database();

async function getScrapes() {
    return database.ref('scrapes').once('value')
}

async function getLastUpdated() {
    return database.ref('last_updated').once('value')
}
