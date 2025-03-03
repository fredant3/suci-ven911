const subContainer = document.querySelector('.subcontainer');
subContainer.classList.add('loading');

window.addEventListener('load',function(){
  subContainer.classList.remove('loading');
});

const baseUrl = "https://raw.githubusercontent.com/rishikumarr/images/main/hand-picked-books/";
const cardTemplate = document.querySelector('[data-card-template]');

const books = [
  [0, "wilder-girls.jpeg","Wilder Chica","Rory Power","Drama","This fresh debut is a mind-bending novel unlike anything you’ve read before. Rory Power’s work is a feminist Lord of the Flies about three best friends living in quarantine at their island boarding school, and the lengths they go to uncover the truth of their confinement when one disappears.",14,true] ,
  [1,"the-between.jpeg","The Between","David Hofmeyr","Fiction","Seventeen-year-old Ana Moon is having a rough week. It starts with a fight after school, then suspension, followed by mandatory psych visits. Still, Ana hopes therapy will help her with another problem–the disturbing feeling that someone, or something, is following her.",16,true],
  [2,"our-italian-summer.jpeg","Our Italian Summer","Jennifer Probst","Romance","Workaholic, career-obsessed Francesca is fiercely independent and successful in all areas of her life except one: family. She struggles to make time for her relationship with her teenage daughter, Allegra, and the two have become practically strangers to each other. When Allegra hangs out with a new crowd and is arrested for drug possession, Francesca gives in to her mother’s wish that they take one epic summer vacation to trace their family roots in Italy. She just never expected to face a choice that might change the course of her life.",24,false],
  [3,"little-life.jpeg", "A Little Life","Yanagihara","Biography","A Little Life follows four college classmates—broke, adrift, and buoyed only by their friendship and ambition—as they move to New York in search of fame and fortune. A hymn to brotherly bonds and a masterful depiction of love in the twenty-first century, Hanya Yanagihara’s stunning novel is about families we are born into, and those that we make for ourselves.",18,true],
  [4,"great-miracle.jpeg","Great Miracle","Maggie Shipsted","Fiction","The unforgettable story of a daredevil female aviator determined to chart her own course in life, at any 'cost'—Great Circle “soars and dips with dizzying flair.","22",true],
  [5,"all-the-bright-places.jpeg","All the Bright Places","Jennifer Niven","Romance","When Theodore Finch and Violet Markey meet on the ledge of the bell tower at school, it’s unclear who saves whom. And when they pair up on a project to discover the “natural wonders” of their state, both Finch and Violet make even more important discoveries. But as Violet’s world grows, Finch’s begins to shrink.",14,true],
  [6,"girl-in-the-translation.jpeg","Girl in Translation","Jean Kwok","Drama","When Kimberly Chang and her mother emigrate from Hong Kong to Brooklyn squalor, she quickly begins a secret double life: exceptional schoolgirl during the day, Chinatown sweatshop worker in the evenings. Disguising the more difficult truths of her life—like the staggering degree of her poverty, the weight of her family’s future resting on her shoulders, or her secret love for a factory boy who shares none of her talent or ambition—Kimberly learns to constantly translate not just her language but herself back and forth between the worlds she straddles.",18,true],
  [7,"big-little-lies.jpeg","Big Little Lies","Liane Moriarty","Thriller","A murder…A tragic accident…Or just parents behaving badly? What’s indisputable is that someone is dead. Big Little Lies is a brilliant take on ex-husbands and second wives, mothers and daughters, schoolyard scandal, and the little lies that can turn lethal.","20",true],
  [8,"arrival.jpeg","Arrival","Ted Chiang","Fantasy","Offering readers the dual delights of the very strange and the heartbreakingly familiar, Arrival presents characters who must confront sudden change. In “Story of Your Life,” which provides the basis for the film Arrival, alien lifeforms suddenly appear on Earth. When a linguist is brought in to help communicate with them and discern their intentions, her new knowledge of their language and its nonlinear structure allows her to see future events and all the joy and pain they may bring.",26,true],
  [9,"moral-compass.jpeg","Moral Compass","Danielle Steel","Fiction","Saint Ambrose Prep is a place where the wealthy send their children for the best possible education, with teachers and administrators from the Ivy League, and graduates who become future lawyers, politicians, filmmakers, and CEOs. Traditionally a boys-only school, Saint Ambrose has just enrolled one hundred and forty female students for the first time. Even though most of the kids on the campus have all the privilege in the world, some are struggling, wounded by their parents’ bitter divorces, dealing with insecurity and loneliness. In such a heightened environment, even the smallest spark can become a raging fire.",18,false],
  [10,"luck-of-the-titanic.jpeg","Luck of the Titanic","Stacey Lee","Drama","From the 'author' of The Downstairs Girl comes the richly imagined story of Valora and Jamie Luck, twin British-Chinese acrobats traveling aboard the Titanic on its ill-fated maiden voyage.",22,false],
  [11,"the-disappearing-act.jpeg","Disappearing Act","Catherine","Thriller","A British actress discovers the dark side of Hollywood when she is the only witness to the sudden disappearance of a woman she meets at an audition in this electrifying psychological thriller.",24,true]
]


books.forEach((book)=>{
  const card = document.importNode(cardTemplate.content,true);
  const [id,image,title,author,genre,description,price,available] = book;
  card.querySelector('img').id = id;
  card.querySelector('img').src=`${baseUrl+image}`; 
  card.querySelector('[data-title]').textContent = title;
  card.querySelector('[data-genre]').textContent = genre;
  card.querySelector('[data-author]').textContent = author;
  subContainer.appendChild(card);   
});
