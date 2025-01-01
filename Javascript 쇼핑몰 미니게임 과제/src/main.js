//Fetch the items from the JSON file
function loadItems(){
    return fetch('data/data.json')
        .then(response => response.json())
        .then(json => json.items);
}


//Create HTML list item from the given data item
function createHTMLString(item){
    return `
    <li class="item" data-type="${item.type}" data-color="${item.color}">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

function displayItems(items){
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

function onButtonClick(event, items){
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key == null || value == null){
        return;
    }
    updateItems(key, value);
}

function updateItems(key, value){
    const items = document.querySelectorAll('.item');
    items.forEach(item => {
        if (item.dataset[key] === value){
            item.classList.remove('invisible');
        } else{
            item.classList.add('invisible');
        }
    });
}

function setEventListeners(items){
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', event => onButtonClick(event, items));
}

//main
loadItems()
    .then(items => {
        displayItems(items);
        setEventListeners(items)
    })
    .catch(console.log)