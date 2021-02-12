async function getScrapes() {
    const config = {
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
    firebase.initializeApp(config);

    const database = firebase.database();
    return database.ref('scrapes').once('value')
}
