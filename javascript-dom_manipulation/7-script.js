fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(function (response) {
    return response.json();
})
.then(function (data) {
    data.results.forEach(function (movie){
        const newLi = document.createElement('li');
        newLi.textContent = movie.title;
        document.querySelector('#list_movies').appendChild(newLi);
    })
})
.catch(function (error) {
    console.error('Error:', error);
})
