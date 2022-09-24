import sys
from urllib.parse import urlencode, parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Derniers Ajouts': [{'name': 'Ne dis rien (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/leZ2tQy4lXeD7CUiRlcZ8UzdMl1.jpg',
						'video': 'https://toma765.tomacloud.com/files/q8dQWFFyveZCETsDjIowThntv0oS8E1yNep.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Abandoned (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/9im8JhelZGDbDpXTigJbjMQqy3S.jpg',
						'video': 'https://toma51.tomacloud.com/files/dUT8YSXRFlxmUJjGMWoZ6bD8fl4NvsTJnMR.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Wolf (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/lw7knnuSLwYoFvKcDaotcgQ3CRf.jpg',
						'video': 'https://toma804.tomacloud.com/files/vB9v4psdiqlQO3gz6c04HjdO06xP8tjD5t9.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'J\'adore ce que vous faites (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/dwQLHMpuUlN3yIIpjIkb6vWeD0n.jpg',
						'video': 'https://toma279.tomacloud.com/files/wqU2Fw8Pzx2bGB5RlnlsAL0CcW1sVewrEru.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Restart The Earth (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/kl80N1g69v9QXe1wvkFza31WhD4.jpg',
						'video': 'https://toma655.tomacloud.com/files/h8YT1usGr63uknZ8nOsuxtD58Y1RmMFDVEx.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Ghoster, le fantôme aux miroirs (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/3ui7b1jHCtSMqNJ1ANfSvLrRBCt.jpg',
						'video': 'https://toma187.tomacloud.com/files/EPf8uBPzjV7tlTvMUuMmKOTHAGWDGghk6ws.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'El Lobo : Le pensionnat (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/fI3b62dGu5twc6nu2ZERHuFiamN.jpg',
						'video': 'https://toma804.tomacloud.com/files/p0kC3ivqe59yu7fWsGGWb1UHj5TK2CMrD63.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Hors du monde (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/brP1Yl1JBZhZj408FCrbklJkHbT.jpg',
						'video': 'https://toma621.tomacloud.com/files/wO0awUHw3CTfTWwK1AyTrjwUyJfEKYcgMdq.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Coupez ! (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/sOCMpVoR8Q8zdpS5JQjjqfQ72na.jpg',
						'video': 'https://toma794.tomacloud.com/files/9vDn1q4UkIEsBvKTlcKbP4Cek4ef55xeBbC.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'L\'Été nucléaire (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/uDQptpEmk2RbfEcVfARLMOp5wua.jpg',
						'video': 'https://toma57.tomacloud.com/files/NbdLTk0m1H0kvadmfKcR5HXjeGhuN6sAiGm.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Le Parfumeur (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/ieivbB7SDenOGfqae0vZdJQfJA.jpg',
						'video': 'https://toma621.tomacloud.com/files/e5VWZMBVDxE8msLwxNncnyU0HjTRgKCvQxr.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Entre deux feux (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/ft6sTxzqqe4pZps7X8n5TNpxbhC.jpg',
						'video': 'https://toma664.tomacloud.com/files/JY5KBDNtNRPviSDpx849GRsAJONBgx10w6K.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Joyeuse fin du monde (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/bfUO1SBTfgcK77em3lOuRFY2uLc.jpg',
						'video': 'https://toma735.tomacloud.com/files/JRu7qcFRwe7ZsDNMdY8memHUC4DMPVYyMtF.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Dangerous (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/vTtkQGC7qKlSRQJZYtAWAmYdH0A.jpg',
						'video': 'https://toma468.tomacloud.com/files/0paRC0OaFgj63n0A4Tap134Tmy2YzinzHyr.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Vortex (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/p13QdFAbWacMfGWlZBaOZeN7BHh.jpg',
						'video': 'https://toma641.tomacloud.com/files/6VcKI2FHBsagGPBM0aZbcQa0U8WlkftrbGb.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': '500 mètres sous terre (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/jhdXBFB9IORznMg3nU5n7llFTMf.jpg',
						'video': 'https://toma620.tomacloud.com/files/26piBmECdtrqbeIXUNE50BvWMNOYy0XB6nT.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Le Bal de l\'Enfer (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/kuHvnvP5zBkazEuI3WcuanDd83D.jpg',
						'video': 'https://toma50.tomacloud.com/files/Ax7xTrMnTY44SNVu7egIeRW1tkNhUpfuXm1.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'J\'irai au bout de mes rêves (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/3Izez1AXbEgh3tFQfafOM8Dmuv7.jpg',
						'video': 'https://toma629.tomacloud.com/files/kEbSF9uMwnugVOcXAAbBGmxAcxuD4kRoZ2h.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Broad Peak (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/n7eiUpUb27Vpd3MBfLro9rkUo0F.jpg',
						'video': 'https://toma629.tomacloud.com/files/YNXowjPN5lVamWA7txp0KlqdZt7pweOv2LT.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'La Scuola Cattolica (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/4r7ssCjVvUg5yHFivv3OUmIWNNU.jpg',
						'video': 'https://toma320.tomacloud.com/files/2M1xq5SitRkKxxvYgETfIDrLYdYVGypJlrg.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Goodnight Mommy (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/oHhD5jD4S5ElPNNFCDKXJAzMZ5h.jpg',
						'video': 'https://toma28.tomacloud.com/files/EPixpmgMxk4SLjNj1ghKuzTVSvuAFh7j7pR.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Miroir, miroir (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/3FUfdBpl7VjC0ZWAbhLMcave9Ar.jpg',
						'video': 'https://toma708.tomacloud.com/files/IeEPE4OhkknyI59OXUJh8Wr2C9Ci78MPnqE.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Si tu me venges (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/akIjKJDHcVN4bzifcEarKVPNpoa.jpg',
						'video': 'https://toma620.tomacloud.com/files/ScQxuXQBnI99PsthQFtxF0gWNKIa6qqZCgw.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Les Murs vagabonds (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/goOdPcILnfOMk5ocrjCLpJOt8zY.jpg',
						'video': 'https://toma620.tomacloud.com/files/p7MHXtAziI2KzEEW6qndBbJFrGd9yVWX3IF.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Le chemin du bonheur (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/eLNXmZgfxiH3etaQLkMH7o2wq1j.jpg',
						'video': 'https://toma708.tomacloud.com/files/pHAN7fPCI9swQR3EpnpSrrusU94xqZiPHSC.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Cœurs vaillants (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/2r5rMqJxMqqlIqMiHXi0tLN5H9x.jpg',
						'video': 'https://toma655.tomacloud.com/files/jeOvuoZs1e0i7uGrmhmqDWVFKzgubPhu350.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Le Samaritain (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/iX69aMEMO0W22bAX11lGP8DeTkr.jpg',
						'video': 'https://toma288.tomacloud.com/files/6d5RNllYaDtdJtLdtLJIMy5h3TaQ3sf9Gk0.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Beckenrand Sheriff (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/knYcXhKLLIP6GtyuvcZxLp59P8a.jpg',
						'video': 'https://toma629.tomacloud.com/files/MXINro9Te8OiRd7N6ItI5HpKZZA7CSvpQec.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Le Royaume de Terracotta (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/xbsgNAg021mKIbj2mBvB3LzvYVP.jpg',
						'video': 'https://toma28.tomacloud.com/files/tacGsP2DHxDSURb4bcIdk3Fco7FRbZPFa1m.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'The Aviary (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/u6HUQcOQsgkFFO8xCITfxQz6ivc.jpg',
						'video': 'https://toma654.tomacloud.com/files/QU6RRRTfFTipPUmrj55Xa2BNdL0aHtdyojq.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Sword Master (2016) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/sCsFOWDTETklLlVj34msCn0S6JP.jpg',
						'video': 'https://toma877.tomacloud.com/files/3YEVWzcENM3dli0zdvyLNg6Ts21WK1oOZ2K.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Petite fleur (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/lMO0n5CAMRftZGebjTCXmufuJiZ.jpg',
						'video': 'https://toma641.tomacloud.com/files/GQlG03aeByx1NIliyy5OBMr5M9FL2ilI8Hp.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Beast (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/iRV0IB5xQeOymuGGUBarTecQVAl.jpg',
						'video': 'https://toma400.tomacloud.com/files/EFV0n4HNdrnANwwasaTHna1o27R00uDF9zF.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'End of the Road (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/tLFIMuPWJHlTJ6TN8HCOiSD6SdA.jpg',
						'video': 'https://toma187.tomacloud.com/files/9BWsoQ2JX1bZYohcbEs0IYQgsOYiqGUziR2.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'The Captain (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/jG82eg6xnG95XuR6Tqn6GjXytQI.jpg',
						'video': 'https://toma620.tomacloud.com/files/6TXKgiA512Hg0tX89mD0MxTkjNTzk7Zr1Wc.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Trois mille ans à t\'attendre (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/eCYaYduejXz9SIkLsKkHESU1sWq.jpg',
						'video': 'https://toma468.tomacloud.com/files/zcRyuhfoRxgUeXZGC6jhakdswNdJ6WMF9Ee.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Don Juan (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/gsy1V0FRqa9yfgbc8PuGHZE1kL1.jpg',
						'video': 'https://toma627.tomacloud.com/files/BCWKgaocDq0EIIUYqQQe60cGnEMyiBOUdKE.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Pinocchio (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/h32gl4a3QxQWNiNaR4Fc1uvLBkV.jpg',
						'video': 'https://toma664.tomacloud.com/files/VyXdaL7owMSsPy1ifftFpDvpEzvFQh5LQ2Z.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Thor : Love And Thunder (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/kSMarEm3ESOOr11dzsep2RZ1ClD.jpg',
						'video': 'https://toma902.tomacloud.com/files/QDptJDzxxbPYnzXXTUhI47Kkj0LYZayPNXj.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Thor : Ragnarok (2017) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/mAA8RXkgF87jSWWMSf6hgLl73mk.jpg',
						'video': 'https://toma288.tomacloud.com/files/rHGxtwzsxnAWJuewd5mebrJXVRePD6d5NUC.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Thor : Le Monde des ténèbres (2013) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/eAIGX0nlwlb5sMb4uDRGNFqMyG9.jpg',
						'video': 'https://toma320.tomacloud.com/files/Q97PjFE7CYFcQKkVFqo8vOwtwCwlsUui3B7.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Thor (2011) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/q8pF6s9b9veTQvxTqMDIQf9nJKi.jpg',
						'video': 'https://toma654.tomacloud.com/files/BkGJHXvbQglWRfmnOeiwA1KqgBNQU5VwqCg.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Sous emprise (2022) ',
						'thumb': 'https://i.imgur.com/AF2sqtm.png',
						'video': 'https://toma654.tomacloud.com/files/e6pAZjjg2gPgNqgMhQyZmqDoHTG7IKRWRhx.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Train de guerre : le corridor de l\'espoir (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/3quDnxahqLnQWYE67xsmVIvDN7D.jpg',
						'video': 'https://toma627.tomacloud.com/files/5DTBsXjER3w9IDGnDA1pL28V4OlOOGxTjru.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'The Ledge (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/dHKfsdNcEPw7YIWFPIhqiuWrSAb.jpg',
						'video': 'https://toma50.tomacloud.com/files/CQqPBRYKIAdk8tt0lAsICW8axCtY9aHL17A.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Inexorable (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/iiclsw6zgRJz5D5Cc6sn4Cs9GQo.jpg',
						'video': 'https://toma708.tomacloud.com/files/4pc3XAK7bNpfjIGptP8b62r1pF4XCTxGjKJ.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Loving Adults (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/mNSqObjKszcxr55buQafQF9ARiC.jpg',
						'video': 'https://toma708.tomacloud.com/files/n6CHRlYcQmH8atJGWLGdUSB6v1HOvhKTomA.mp4',
						'genre': 'Derniers Ajouts'},
						{'name': 'Seoul Vibe (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/ffX0TL3uKerLXACkuZGWhAPMbAq.jpg',
						'video': 'https://toma126.tomacloud.com/files/dPpVEUcpNALnQtWh1RrIW49IEkarruPEkfz.mp4',
						'genre': 'Derniers Ajouts'},

                      ],
            'A l\'affiche': [{'name': 'Pinocchio (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/h32gl4a3QxQWNiNaR4Fc1uvLBkV.jpg',
						'video': 'https://toma664.tomacloud.com/files/VyXdaL7owMSsPy1ifftFpDvpEzvFQh5LQ2Z.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Thor : Love And Thunder (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/kSMarEm3ESOOr11dzsep2RZ1ClD.jpg',
						'video': 'https://toma902.tomacloud.com/files/QDptJDzxxbPYnzXXTUhI47Kkj0LYZayPNXj.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Top Gun : Maverick (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/uuwi4wwG6HAHVqaEvJDx6gI773N.jpg',
						'video': 'https://toma122.tomacloud.com/files/5uCpwiTL7cEe6Er6UGMRNcLxi1jMSmtYQ5o.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Elvis (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/mTzwJL0ENwqIuMNGp2q6vkK3yis.jpg',
						'video': 'https://toma664.tomacloud.com/files/P3yRcI67d9GwPK32zTPpc8khSztg0viQyQH.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Prey (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/8qlGO9zM1ysyw2xzsWfYMgnd2KT.jpg',
						'video': 'https://toma57.tomacloud.com/files/LHMlDoeH1BeFA7nMUKD4vfqrZnmDhMV2uHo.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Buzz l\'Éclair (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/5aM7y4Du4whbTCx4GafQXKj14xi.jpg',
						'video': 'https://toma621.tomacloud.com/files/P0bLoiyWC4Gv933CDMTAUJJK82MC1EOQEZC.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Les Minions 2 : Il était une fois Gru (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/ucLdEGaIFlpIdGlkzYj2OcXbGhz.jpg',
						'video': 'https://toma50.tomacloud.com/files/A1dc4wn3rCIS1rm3NDYJPDoKp7tPQP2rRgE.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Jurassic World : Le Monde d\'après (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/4tRxeoxwf6X8l3yWYJr1CniKm6O.jpg',
						'video': 'https://toma877.tomacloud.com/files/HOO7HKNR5ZV326P7V86gjfY9WS12G95nXUu.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Doctor Strange in the Multiverse of Madness (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/dbJDPJBHKxnMyvcc12mcbGK5RPF.jpg',
						'video': 'https://toma28.tomacloud.com/files/juXjjUE2igCxduW5ca4udFIFXXKcNdp7Imr.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Les Animaux Fantastiques : Les Secrets de Dumbledore (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/uXs7wMtsfnBFuGVogAxJXZXshFU.jpg',
						'video': 'https://toma654.tomacloud.com/files/590GPpKRQM2VcbelLqklDblaL4YxRGQWPQC.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Sonic 2, le film (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/7RSCL6V8BlekgVnNPok6tLW50tP.jpg',
						'video': 'https://toma522.tomacloud.com/files/sgYva3hyttIstJLGHW4dZkuVnU55PpwhGuN.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Morbius (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/xBoIe0eX9UuSSPe5Qt6KXIQOd3I.jpg',
						'video': 'https://toma28.tomacloud.com/files/ZwwSu3Qf2oinl2FHjFobPQGkp3w3oGOoclh.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'The Northman (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/hk0JZyTHfgN35f43pJUhDPTNjM0.jpg',
						'video': 'https://toma28.tomacloud.com/files/j6I21h19ADP0VDnrrbitqS3afgUGXxZgEHj.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Ambulance (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/bvFeEZ10Gtt5Yd2KKDOTaO4m8v7.jpg',
						'video': 'https://toma512.tomacloud.com/files/BC0TaLT8VjIaNR86z1ZCa0U2TKAVeZOPBPJ.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Uncharted (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/yd12LPRc6X7dZvSMo57xbXVGk3G.jpg',
						'video': 'https://toma320.tomacloud.com/files/LdowVVivA1T7Ccx6LQ6n1F5bQW7u9Y7Ucvr.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'The Batman (2022) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/8gVy5MLXtZBWghMykQtPMsNc5kH.jpg',
						'video': 'https://toma320.tomacloud.com/files/A8LRYdDKhUqdnPEC8hNiobFIJdoTJTnj18b.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Spider-Man: No Way Home (2021) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/j5f5bRlpChRuyHdexmeSnQmklDt.jpg',
						'video': 'https://toma629.tomacloud.com/files/2qGpfwTsSfJcZjO957YpdJC35CY9YKa1aRr.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'The King’s Man - Première Mission (2021) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/tENLxofTH3ZiJyaqfVH37oQaFez.jpg',
						'video': 'https://toma877.tomacloud.com/files/an9Wb7QKP9F12w3Zb6vWerodfMwOinWtK6p.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'House of Gucci (2021) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/cy6fvTf9YqehVhReYnm5cc3GqhZ.jpg',
						'video': 'https://toma641.tomacloud.com/files/NoL9ANQ8SSNsCXhZlpA7rJKts4T1Tg9GEUQ.mp4',
						'genre': 'A l\'affiche'},
						{'name': 'Clifford (2021) ',
						'thumb': 'https://www.themoviedb.org/t/p/original/dtVB6o5ZUnyRTu3SsFqqcHdGbzU.jpg',
						'video': 'https://toma126.tomacloud.com/files/HwnuKMrwE0w7uJsDHMaZVHsFGrJR357KBue.mp4',
						'genre': 'A l\'affiche'},


                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or API.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or API.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
