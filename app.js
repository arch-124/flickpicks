let left_btn = document.getElementsByClassName('bi-chevron-left')[0];
let right_btn = document.getElementsByClassName('bi-chevron-right')[0];
let cards = document.getElementsByClassName('cards')[0];

left_btn.addEventListener('click',()=>{
    cards.scrollLeft -= 140;
})
right_btn.addEventListener('click',()=>{
    cards.scrollLeft += 140;
})
let json_url = "movie.json";
fetch(json_url).then(Response => Response.json())
    .then((data ) => {
        data.forEach((ele, i) => {
            let { name, imdb, date, sposter, bposter, genre} = ele;
            let card = document.createElement('a');
            card.classList.add('card');
            card.innerHTML = `
            <img src ="${sposter}" alt="${name}" class="poster">
            <div class="rest_card">
                <img src="${bposter}" alt="">
                <div class="cont">
                    <h4>${name}</h4>
                    <div class="sub">
                        <p>${genre}, ${date}</p>
                        <h3><span>IMBD</span> <i class="bi bi-star-fill"></i>${imdb}</h3>
                    </div>
                </div>
            </div>
            `
           /* cards.appendChild(card); */
        });

        document.getElementById('title').innerText = data[0].name;
        document.getElementById('gen').innerText = data[0].genre;
        document.getElementById('date').innerText = data[0].date;
        document.getElementById('rate').innerText =`<span>IMBD</span> <i class="bi bi-star-fill"></i> ${data[0].imdb}`
    })
        
        let series = document.getElementById('series');
        let movies = document.getElementById('movies');
        let anime = document.getElementById('anime');


        series.addEventListener('click', () => {
           cards.innerHTML =  '';

           let series_array = data.filter(els => {
                return ele.type === "series";
           });

           series_array.forEach((ele, i) => {
            let { name, imdb, date, sposter, bposter, genre} = ele;
            let card = document.createElement('a');
            card.classList.add('card');
            card.innerHTML = `
            <img src ="${sposter}" alt="${name}" class="poster">
            <div class="rest_card">
                <img src="${bposter}" alt="">
                <div class="cont">
                    <h4>${name}</h4>
                    <div class="sub">
                        <p>${genre}, ${date}</p>
                        <h3><span>IMBD</span> <i class="bi bi-star-fill"></i>${imdb}</h3>
                    </div>
                </div>
            </div>
            `
            cards.appendChild(card);
        });
    })
        movies.addEventListener('click', () => 
        {
            cards.innerHTML =  '';
 
            let movies_array = data.filter(els => 
            {
                 return ele.type === "movies";
            });
 
            movies_array.forEach((ele, i) =>
            {
             let { name, imdb, date, sposter, bposter, genre} = ele;
             let card = document.createElement('a');
             card.classList.add('card');
             card.innerHTML = `
             <img src ="${sposter}" alt="${name}" class="poster">
             <div class="rest_card">
                 <img src="${bposter}" alt="">
                 <div class="cont">
                     <h4>${name}</h4>
                     <div class="sub">
                         <p>${genre}, ${date}</p>
                         <h3><span>IMBD</span> <i class="bi bi-star-fill"></i>${imdb}</h3>
                     </div>
                 </div>
             </div>
             `
             cards.appendChild(card);
            });
        })  
        anime.addEventListener('click', () => 
            {
                cards.innerHTML =  '';
     
                let anime_array = data.filter(els => 
                {
                     return ele.type === "anime";
                });
     
                anime_array.forEach((ele, i) =>
                {
                 let { name, imdb, date, sposter, bposter, genre} = ele;
                 let card = document.createElement('a');
                 card.classList.add('card');
                 card.innerHTML = `
                 <img src ="${sposter}" alt="${name}" class="poster">
                 <div class="rest_card">
                     <img src="${bposter}" alt="">
                     <div class="cont">
                         <h4>${name}</h4>
                         <div class="sub">
                             <p>${genre}, ${date}</p>
                             <h3><span>IMBD</span> <i class="bi bi-star-fill"></i>${imdb}</h3>
                         </div>
                     </div>
                 </div>
                 `
                 cards.appendChild(card);
                });
            })
            
 


