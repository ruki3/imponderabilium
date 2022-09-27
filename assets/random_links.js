// Here is where you list your pages! You can use either ABSOLUTE or RELATIVE links. If you're not sure the difference, I recommend using full links starting with 'https://'

// here's where we list the pages. The first item is the URL and the second item is the title.
var webPages = [
            ["https://yesterweb.org/community/", "The Yesterweb Community"],
            ["https://yesterweb.org/link-directory/", "Link Directory"],
            ["https://yesterweb.org/zine/", "The Yesterweb Zine"],
            ["https://yesterweb.org/webring/", "The Yesterweb Webring"],
            ["https://yesterweb.org/radio/", "The Yesterweb Radio"],
            ["https://yesterweb.org/manifesto/", "Internet Manifestos"],
            ["https://yesterweb.org/bb/", "Bulletin Board"],
            ["https://yesterweb.org/community/gemini.html", "Gemini"],
            ["https://yesterweb.org/community/cafe/", "Yesterweb Cafe"],
            ["https://yesterweb.org/mascots/", "Yesterweb Mascots"],
            ["https://yesterweb.org/graphics/buttons.html", "88x31 Buttons"]
            ["https://yesterweb.org/no-to-web3/", "Keep the Web Free, Say No to Web3"]
        ]

// this function shuffles the array (reorder the items randomly)
function shuffle(webPages) {
  let currentIndex = webPages.length, randomIndex;

  // while there are items left to shuffle...
  while (currentIndex != 0) {
  // pick a remaining element...
  randomIndex = Math.floor(Math.random() * currentIndex);

  // decrease
  currentIndex--;

  // swap with current element
  [webPages[currentIndex], webPages[randomIndex]] = [webPages[randomIndex], webPages[currentIndex]];
  }
  return webPages;
}

function displayLinks(num) {
  shuffle(webPages);
  
  for (let i = 0; i < num; i++) {
    var link = "<a href='" + webPages[i][0] + "'>" + webPages[i][1] + "</a><br>";
    document.getElementById('randomPages').innerHTML += link;
   }
}

/* below is the code that executes our program 
you can change the '5' number to anything 
as long as it's lower than the total number of links in your array. */

/* it is guaranteed to have no duplicates! */ 
document.addEventListener("DOMContentLoaded", function() {
  displayLinks(5);
});
