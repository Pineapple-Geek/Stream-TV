# Module: main
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Example video plugin that is compatible with Kodi 19.x "Matrix" and above
"""
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
VIDEOS = {'Film': [{'name': 'Fullmetal Alchemist : La vengeance de Scar (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/zr9Kx72QwRYyQqhMOU4ABHydB5k.jpg',
                      'video': 'https://toma400.tomacloud.com/files/hnLscdKRxBnVRzP9ulNUQu52DsBbZHGg4rJ.mp4',
                      'genre': 'Film'},
                      {'name': 'FullMetal Alchemist (2017) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/1KGEyeCNyZFDZVDo1H0S87Re8qT.jpg',
                      'video': 'https://toma804.tomacloud.com/files/TvJgRgwZA0OWfKPs1iBGyNXVGk02TwGM1p3.mp4',
                      'genre': 'Film'},
                      {'name': 'Bullet Proof (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/cj6YmTAU7Jvn3w6d2NfjQzpX7Pw.jpg',
                      'video': 'https://toma51.tomacloud.com/files/51BfH9lXhh3RfteHyVRVuZR0xRehGxdMyO1.mp4',
                      'genre': 'Film'},
                      {'name': 'I Comete (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/nb9lYyc3JdDjHNeGYIMYrRSiylD.jpg',
                      'video': 'https://toma761.tomacloud.com/files/86csIMCh0VdeBxFrhtChjaWoGiLbXyT5E5x.mp4',
                      'genre': 'Film'},
                      {'name': 'Les Sans-dents (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/eECFndv44mSkC9NjI7UYA9j2MU0.jpg',
                      'video': 'https://toma655.tomacloud.com/files/cKdQgi4mxpLToJ66RtoYk8DtiaL5tSRGC5w.mp4',
                      'genre': 'Film'},
                      {'name': 'Les Gagnants (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/bmyRcw8lnOnNlywEPxZVAeEkWGp.jpg',
                      'video': 'https://toma522.tomacloud.com/files/Jd0x53TBxj38uqk1Hk407TojcH40kUb37cB.mp4',
                      'genre': 'Film'},
                      {'name': 'Les Segpa (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/60EgLsQZTxBdRVjIRSh6bJZrSyu.jpg',
                      'video': 'https://toma512.tomacloud.com/files/hA9gXlliS893p53WgPetTgJRV8Fc5qUm03C.mp4',
                      'genre': 'Film'},
                      {'name': 'Rainfall (2009) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/jpcy33dy2fkUeUI45OZuDql1KVx.jpg',
                      'video': 'https://toma50.tomacloud.com/files/Yd2r3Pr48nx7nKua1G291wuKZAvqIK0HX28.mp4',
                      'genre': 'Film'},
                      {'name': 'De nos frères blessés (2022) ',
                      'thumb': 'https://i.imgur.com/EHKTCJF.jpg',
                      'video': 'https://toma877.tomacloud.com/files/CXrkgtCNAoYjFRxt2A9xPq4gj5SS1O5DMxY.mp4',
                      'genre': 'Film'},
                      {'name': 'Babysitter (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/enBsCx6CUco6tHZlo4VaaqOr6cB.jpg',
                      'video': 'https://toma57.tomacloud.com/files/NHpc1epLBt6EioCNEJowouWLzBUVXRTLyjY.mp4',
                      'genre': 'Film'},
                      {'name': 'Allons enfants (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/e0vir9Pl1nPizkUlptCpfxbfBXi.jpg',
                      'video': 'https://toma57.tomacloud.com/files/PtQnr2y1zHewcS3artdDPU7GXTLiNNGDhx1.mp4',
                      'genre': 'Film'},
                      {'name': 'Esther 2 : Les Origines (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/qlJT0deZBto3Sx7s0XHtfvKGV1S.jpg',
                      'video': 'https://toma641.tomacloud.com/files/rHgu5rMaudPJHrHu9OTkFbrR5fKC4tPvb60.mp4',
                      'genre': 'Film'},
                      {'name': 'Esther (2009) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/6w6L9C24517AqyqE1GtZT3HUK8U.jpg',
                      'video': 'https://toma794.tomacloud.com/files/nRwUmETm6EJRliDcSbImqE6hMw8ErSaOJGJ.mp4',
                      'genre': 'Film'},
                      {'name': 'Seobok (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/7sPEI9L5kyR14JijGnuTWiL3kwr.jpg',
                      'video': 'https://toma522.tomacloud.com/files/0kbZpsKaroQickMS9tqk9zduiaUGM7iMstM.mp4',
                      'genre': 'Film'},
                      {'name': 'Virus : 32 (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/tK3ogw4VZ75OgDjViXiAWzD3l8L.jpg',
                      'video': 'https://toma107.tomacloud.com/files/1Jmu7XmB4tL3l4ylNXWjSuY8IHjHMT3ODpj.mp4',
                      'genre': 'Film'},
                      {'name': 'Compétition officielle (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/eQzy8e5j5ZLh4I2JNP5wbhAKLtE.jpg',
                      'video': 'https://toma122.tomacloud.com/files/9VV2eqvNpmg9OaMsRTWfbZjyNxM9T2b3X75.mp4',
                      'genre': 'Film'},
                      {'name': 'White Elephant (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/4U32ULTfEz2c456ukx5HCPDVQQ7.jpg',
                      'video': 'https://toma468.tomacloud.com/files/mHYYc1piDz8OABkakgrGhkDBdZJ16P2tx1r.mp4',
                      'genre': 'Film'},
                      {'name': 'Vengeance (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/pdQFGAX68LWoiBqzXwZhMRaraC0.jpg',
                      'video': 'https://toma126.tomacloud.com/files/wZFI6fN38tAkKT6nrs4L3rbYz9n9WZpsZ5b.mp4',
                      'genre': 'Film'},
                      {'name': 'Royalteen : L héritier (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/oK6I9Wa5RIqxpNbJ4NWemsotcYJ.jpg',
                      'video': 'https://toma187.tomacloud.com/files/L1D35H5sHOEGQAmta7oMkufYOxuwJKfvLSy.mp4',
                      'genre': 'Film'},
                      {'name': 'Une vie ou l autre (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/g0XnDidedm4USR443h56yWiglMu.jpg',
                      'video': 'https://toma28.tomacloud.com/files/hawO9mhZZhEyacQfJFmNi2fYveBV3hilsP9.mp4',
                      'genre': 'Film'},
                      {'name': 'First Love (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/gwLNm5VYq68Q65100uOr5fyAh9A.jpg',
                      'video': 'https://toma126.tomacloud.com/files/FeY7wRvYy4KAUmZFRE5Jm26DX36jJ2OpgNw.mp4',
                      'genre': 'Film'},
                      {'name': 'Tre piani (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/k0IOYlKNluMB67k4hA5RwHhI2Y0.jpg',
                      'video': 'https://toma621.tomacloud.com/files/IWwnhmgmGcKBlWvGsL8HxMQyXQY4V0sDWZ0.mp4',
                      'genre': 'Film'},
                      {'name': 'Claire Andrieux (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/xaYkKGwdDOuPhCLCZiUYb1Y2gXh.jpg',
                      'video': 'https://toma664.tomacloud.com/files/ZdoRJ5TUE6JqivMnmgXIOIbB4FkvrE3qSsi.mp4',
                      'genre': 'Film'},
                      {'name': 'Le Pardon (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/wuzjIYlspeQCMHTPblRRYkbzMYJ.jpg',
                      'video': 'https://toma187.tomacloud.com/files/E0vdkSyhV4aktr53N4S4X5Lqgyc1uEI8Eem.mp4',
                      'genre': 'Film'},
                      {'name': 'Day Shift (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/yQNo9KVTyDzx3NXgyCLqnaZ0k0K.jpg',
                      'video': 'https://toma126.tomacloud.com/files/lPnezUXQsuH0ova6MaocWGfL8FgSlwOHlcV.mp4',
                      'genre': 'Film'},
                      {'name': '13 La comédie musicale (2022) ',
                      'thumb': 'https://i.imgur.com/bQp4nYk.png',
                      'video': 'https://toma522.tomacloud.com/files/jNhelEhb4NbT5mWWxEhHWxWXgbvkVTseGKs.mp4',
                      'genre': 'Film'},
                      {'name': 'Mission Eagle (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/v6xbimngGMkTz72AIBa9pNB8BKE.jpg',
                      'video': 'https://toma107.tomacloud.com/files/Cbx9W5GbwaBt0wv5EnwEuWrvYS7HtgG6rdf.mp4',
                      'genre': 'Film'},
                      {'name': 'Night Raiders (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/oFsw7v3Brx24lPAzu20M8qi4OLE.jpg',
                      'video': 'https://toma28.tomacloud.com/files/pOOcEpfB7cVap00kJreQqnSWCfPvEVL4Jzh.mp4',
                      'genre': 'Film'},
                      {'name': 'Down in Paris (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/7mBkrLDnr0xkNh99oA93atxiIvZ.jpg',
                      'video': 'https://toma902.tomacloud.com/files/goGKtRLUDrPqgsiWu0CcRrlTdzrA81fppV9.mp4',
                      'genre': 'Film'},
                      {'name': 'The Last Son (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/qV8ntQjXgfEQSzviF73lfgfGxEI.jpg',
                      'video': 'https://toma620.tomacloud.com/files/MhXGYgbERv8ffGHRqm5L3q3pbpDqdUe0bbH.mp4',
                      'genre': 'Film'},
                      {'name': 'Bruno Reidal : confession d un meurtrier (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/xYMHI0lks44QPvtnHKhErPOtaj0.jpg',
                      'video': 'https://toma320.tomacloud.com/files/3gyxkeDb7TRvSSojgwP0JzGGAOEUzLFC2da.mp4',
                      'genre': 'Film'},
                      {'name': 'Office Invasion (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/kDC9Q3kiVaxrJijaGeZ8ZB2ZoiX.jpg',
                      'video': 'https://toma50.tomacloud.com/files/Lmv2rSVOC6zXBcgjILOHbkTEJ5mNZ9yKv4M.mp4',
                      'genre': 'Film'},
                      {'name': 'Lena & Snowball (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/Llw9iGzmObrbdv5CAeb3DYVXdv.jpg',
                      'video': 'https://toma664.tomacloud.com/files/ydp6tdXPGZSnk9RS67S97yM9eOkAZLLxYaE.mp4',
                      'genre': 'Film'},
                      {'name': 'Embuscade (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/isCocI3XwPg2u7NPW1KsCeJvQas.jpg',
                      'video': 'https://toma288.tomacloud.com/files/C7urfPlCjAIxsCZCvO9NVORWDrMNDvjfDOH.mp4',
                      'genre': 'Film'},
                      {'name': 'Créatures (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/7F5aNSGRwZMGaNA5FxPFlLIDDhe.jpg',
                      'video': 'https://toma126.tomacloud.com/files/sjYHlw4ECW8n5p3SCYTFLdFbGZtoVMtn6s5.mp4',
                      'genre': 'Film'},
                      {'name': 'Petite leçon d amour (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/cyC4Iw654S1CSxZjk5TIff5kxsh.jpg',
                      'video': 'https://toma902.tomacloud.com/files/ZZ6vq1YaBzHUlyWP4kHOLjyTplQ3IPAHOHd.mp4',
                      'genre': 'Film'},
                      {'name': 'Ma mère est un gorille (et alors?) (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/dow5inuPlfjoMK7OHH0wzWQP4rR.jpg',
                      'video': 'https://toma702.tomacloud.com/files/vhKu5kt413WXC2giTOdwTjC4aR1fkDbQUWl.mp4',
                      'genre': 'Film'},
                      {'name': 'L été l éternité (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/bVVrgwHNqbCJ2sM67VldKnoYdIh.jpg',
                      'video': 'https://toma902.tomacloud.com/files/9DkqgUKkrUXDa2YGOYAdd2icVUM5WA55dpw.mp4',
                      'genre': 'Film'},
                      {'name': 'Elvis (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/mTzwJL0ENwqIuMNGp2q6vkK3yis.jpg',
                      'video': 'https://toma655.tomacloud.com/files/O823WMTIwRYpHB31cfX0vCUiY9RBkJJ8SMb.mp4',
                      'genre': 'Film'},
                      {'name': 'Le dernier patient (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/xlgjB0fISn5767hnQbfR4lkJwP3.jpg',
                      'video': 'https://toma664.tomacloud.com/files/z3hwSbBH54edZjFBH79MdxxXrJdHxA17DiD.mp4',
                      'genre': 'Film'},
                      {'name': 'Abuela (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/tZGoxO2rwfmm5m6oeNjLDORALqy.jpg',
                      'video': 'https://toma122.tomacloud.com/files/zMcd5PKz4Y9orXHdqCH1HXQjLCmjC7ocTBq.mp4',
                      'genre': 'Film'},
                      {'name': 'Le traducteur (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/gTqFVxe1lF98lLNxw63sYxfAzwT.jpg',
                      'video': 'https://toma320.tomacloud.com/files/ydIWpBxPAY08t9QnKvYyBc3I6wGkLhVjuDg.mp4',
                      'genre': 'Film'},
                      {'name': 'Prey (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/8qlGO9zM1ysyw2xzsWfYMgnd2KT.jpg',
                      'video': 'https://toma765.tomacloud.com/files/ek0p8eJP5fDYW2veov09zQFTpfip8cMnwNM.mp4',
                      'genre': 'Film'},
                      {'name': 'Luck (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/1HOYvwGFioUFL58UVvDRG6beEDm.jpg',
                      'video': 'https://toma627.tomacloud.com/files/yJtSTTZvMm2qjJkJI4Qa8OqvJS6fC0ZbJs4.mp4',
                      'genre': 'Film'},
                      {'name': 'LEGO Star Wars - C est l été ! (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/dzPbH4B2xlN1ClxsT8Qh5r5qNRs.jpg',
                      'video': 'https://toma126.tomacloud.com/files/yPjq1AKb4Dk5e3COD8ivg0b9l5YYYlHwb1W.mp4',
                      'genre': 'Film'},
                      {'name': 'Le Destin des Tortues Ninja : Le film (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/4PASAPJSoUsY6I69gaED4k642Gb.jpg',
                      'video': 'https://toma621.tomacloud.com/files/S5l3UU8sZ4ZuI72nsQ0Oag4NuuhjfuS7Aeb.mp4',
                      'genre': 'Film'},
                      {'name': 'Carter (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/yVGSH5HTTnxJ3SlkDNA8xYP3Gu3.jpg',
                      'video': 'https://toma761.tomacloud.com/files/tgVKAafshPHtkQNiXbezjieOPJkap6BTmwE.mp4',
                      'genre': 'Film'},
                      {'name': 'Treize vies (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/tgbfXKmK4LPPUniWE8novCPE6xR.jpg',
                      'video': 'https://toma621.tomacloud.com/files/J5UtyY7U2g2rrCamvDYtWMA30cV5V1OE6I8.mp4',
                      'genre': 'Film'},
                      {'name': 'Sniper : Rogue Mission (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/jSL5TqroJsDAIgBdELBwby1uhf1.jpg',
                      'video': 'https://toma664.tomacloud.com/files/WYz3HHHoWg8sSjq6FJPF23B6QBbQvlLskkv.mp4',
                      'genre': 'Film'},
                      {'name': 'Wedding Season (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/mFeXAZ1oOECPqEu8c2i4L5LmNyY.jpg',
                      'video': 'https://toma51.tomacloud.com/files/gOnA9TCb63aACBXutq24JgI54riumlqDaOd.mp4',
                      'genre': 'Film'},
                      {'name': 'Escape From Mogadishu (2022) ',
                      'thumb': 'https://www.themoviedb.org/t/p/original/grFDK4ddh2IMn464Ve4ke4uz2ao.jpg',
                      'video': 'https://toma320.tomacloud.com/files/eUfgrJneRtX24UAcSjSHGtVjmy4qZd1d8ht.mp4',
                      'genre': 'Film'}

                      ],
            'Author': [{'name': 'PineApple-Geek',
                      'thumb': 'https://cdn.ufind.name/fb/webp/100011251727060.webp',
                      'video': 'http://www.vidsplay.com/wp-content/uploads/2017/05/bbqchicken.mp4',
                      'genre': 'Author'}
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
