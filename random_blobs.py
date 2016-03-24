import random

blubs = ['j my b', 
	     'j the b', 
	     'b the b', 
	     'space invaders', 
	     'tictactoe', 
	     'blod', 
	     'russell wilson', 
	     'uhhhh', 
	     'arcade fire', 
	     'arcade lier', 
	     'arcade lion', 
	     'arcade lyer', 
	     'arcade pyre', 
	     'i should\'ve arcade inspired'
	     ]

blobs = ['http://static3.techinsider.io/image/55ba6d1f371d22dd2e8ba492-1106-1012/screen%%20shot%%202015-07-30%%20at%%202.31.57%%20pm.png',
		 'http://i.imgur.com/mUWtowV.jpg',
		 'https://img.buzzfeed.com/buzzfeed-static/static/2015-05/11/14/campaign_images/webdr02/1272-rare-pepes-2-32128-1431369756-0_dblbig.jpg',
		 'https://img.buzzfeed.com/buzzfeed-static/static/2015-10/27/17/enhanced/webdr11/enhanced-mid-29607-1445980104-1.jpg',
		 'https://img.buzzfeed.com/buzzfeed-static/static/2015-10/27/17/campaign_images/webdr06/what-is-the-market-value-of-a-rare-pepe-2-28727-1445981181-8_big.jpg',
		 'http://static.fjcdn.com/pictures/Rare+pepe+s+get+yer+rare+pepe+s+here_5a814b_5507279.jpg',
		 'http://static.fjcdn.com/pictures/Rare_1d0057_5507279.jpg',
		 'http://static.fjcdn.com/pictures/Rare_2b6c68_5507279.jpg',
		 'http://static.fjcdn.com/pictures/Rare_a41f3a_5507279.jpg',
		 'http://static.fjcdn.com/pictures/Rare_7b92c8_5507279.jpg',
		 'http://static.fjcdn.com/pictures/Rare_26283b_5507279.jpg',
		 ]

def randomize(blib):
	temp = random.randrange(0, len(blib))
	return blib[temp]
