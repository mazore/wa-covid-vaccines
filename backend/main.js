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

const container = document.createElement('div');
const list = document.createElement('ul');
document.getElementsByTagName('body')[0].appendChild(container);
container.appendChild(list);

const database = firebase.database();
database.ref('scrapes').once('value').then((snapshot) => {
    const scrapes = snapshot.val();
    for (const name in scrapes) {
        addListItem(scrapes[name]);
    }
});

function addListItem(data) {
    const item = document.createElement('li');
    item.innerHTML = `${data.name} <a href="${data.url}" class="sign-up">Sign Up</a>`;
    item.classList.add('item')
    list.appendChild(item);
}
