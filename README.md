# deck-docker
A sample application<br>
A Card Deck game that allows users to shuffle the deck and deal a card<br>
It is built on Oracle Linux, Python and Flask<br>

Download this onto your docker node (git clone https://github.com/sundeepdhall/deck-docker.git)

To build this docker image<br>
"docker build -t deck-docker:latest ."<br><br>
To run this docker image<br>
"docker run -p port:80 -t deck-docker"<br>

##Sample Output
<center><b>Card Game</b></center> <br>["AS", "JS", "QS", "KS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "AH", "JH", "QH", "KH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "AD", "JD", "QD", "KD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "AC", "JC", "QC", "KC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C"]<br> <b>deal shuffle reset</b>
