screen daftarisi():

    tag menu
   
    imagemap:
        #add "menu_ground.png"
        ground "chapter/menu_idle.png"
        hover "chapter/menu_hover.png"

        hotspot (52,39,160,78) action Start("prolog")
        hotspot (52,132,160,75) action Start("chapter1")
        hotspot (52,132,160,75) action Start("chapter1")
        hotspot (52,211,160,75) action Start("chapter2")
        hotspot (52,287,179,75) action Start("chapter3")
        hotspot (52,371,160,75) action Start("chapter4")
        hotspot (52,493,160,75) action Start("quiz")
        hotspot (58,606,110,43) action Return()
