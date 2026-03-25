document.querySelector('#add_item').addEventListener('click', function () {
    const newItem = document.createElement('li');
    document.querySelector('.my_list').appendChild(newItem);
    newItem.textContent = 'Item';
});
