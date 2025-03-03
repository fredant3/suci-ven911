const subContainer = document.querySelector('.subcontainer');
subContainer.classList.add('loading');

window.addEventListener('load',function(){
  subContainer.classList.remove('loading');
});

const baseUrl = "https://raw.githubusercontent.com/rishikumarr/images/main/hand-picked-books/";
const cardTemplate = document.querySelector('[data-card-template]');

const books = [
  [0, "wilder-girls.jpeg","Wilder Chica","Rory Power","Drama"] ,
  [1,"the-between.jpeg","The Between","David Hofmeyr","Fiction"],
  [2,"our-italian-summer.jpeg","Our Italian Summer","Jennifer Probst","Romance"],
  [3,"little-life.jpeg", "A Little Life","Yanagihara","Biography"],
  [4,"great-miracle.jpeg","Great Miracle","Maggie Shipsted","Fiction"],
  [5,"all-the-bright-places.jpeg","All the Bright Places","Jennifer Niven","Romance"],
  [6,"girl-in-the-translation.jpeg","Girl in Translation","Jean Kwok","Drama"],
  [7,"big-little-lies.jpeg","Big Little Lies","Liane Moriarty","Thriller"],
  [8,"arrival.jpeg","Arrival","Ted Chiang","Fantasy"],
  [9,"moral-compass.jpeg","Moral Compass","Danielle Steel","Fiction"],
  [10,"luck-of-the-titanic.jpeg","Luck of the Titanic","Stacey Lee","Drama"],
  [11,"the-disappearing-act.jpeg","Disappearing Act","Catherine","Thriller"]
]


books.forEach((book)=>{
  const card = document.importNode(cardTemplate.content,true);
  const [id,image,title,author,genre] = book;
  card.querySelector('img').id = id;
  card.querySelector('img').src=`${baseUrl+image}`; 
  card.querySelector('[data-title]').textContent = title;
  card.querySelector('[data-genre]').textContent = genre;
  card.querySelector('[data-author]').textContent = author;
  subContainer.appendChild(card);   
});
