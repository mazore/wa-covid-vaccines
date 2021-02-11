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
    const btn = document.createElement('a');
    btn.innerText = 'Sign Up';
    btn.href = data.url;
    btn.classList.add('btn');

    const p1 = document.createElement('p')
    p1.innerText = (data.num_appointments ?? 0) + ' appointments available';
    p1.classList.add('info')

    const p2 = document.createElement('p');
    const secsAgo = Math.round(Date.now()/1000 - data.time);
    p2.innerText = `Last checked ${secsAgo} seconds ago`;
    p2.classList.add('info')

    const item = document.createElement('li');
    item.innerText = data.name;
    item.classList.add('item');
    item.appendChild(btn);
    item.appendChild(p1);
    item.appendChild(p2);
    if (data.available) {
        item.style.border = '1px solid green';
    } else {
        item.style.border = '1px solid red';
    }

    list.appendChild(item);
}
