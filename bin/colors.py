class Color:

    def __init__(self):
        
        self.black = [0,0,0]
        self.gray = [128,128,128]
        self.white = [255,255,255]
        self.purple = [128,0,128]
        self.blue = [0,0,255]
        self.green = [0,128,0]
        self.pink = [255,192,203]
        self.yellow = [255,255,0]
        self.red	= [255,0,0]
        self.lavender = [230,230,250]
        

#         # Tons de Cinza
#         black = [0,0,0]
#         dimgray = [105,105,105]
#         gray = [128,128,128]
#         darkgray = [169,169,169]
#         silver = [192,192,192]
#         lightgrey =	[211,211,211]
#         gainsboro = [220,220,220]
#         white = [255,255,255]

#         # Tons de Azul
#         slateblue =	[106,90,205]
#         darkslateblue =	[72,61,139]
#         midnightblue = [25,25,112]
#         navy = [0,0,128]
#         darkblue = [0,0,139]
#         mediumblue = [0,0,205]
#         blue = [0,0,255]
#         cornflowerblue = [100,149,237]
#         royalblue = [65,105,225]
#         dodgerblue = [30,144,255]
#         deepskyblue	= [0,191,255]
#         lightskyblue = [135,206,250]
#         skyblue = [135,206,235]
#         lightblue =	[173,216,230]
#         steelblue = [70,130,180]
#         lightsteelblue = [176,196,222]
#         slategray = [112,128,144]
#         lightSlateGray = [119,136,153]

#         # Tons de Roxo
#         purple = [128,0,128]
#         magenta	= [255,0,255]
#         mediumslateblue	= [123,104,238]
#         mediumpurple = [147,112,219]
#         blueviolet = [138,43,226]
#         indigo = [75,0,130]
#         darkviolet = [148,0,211]
#         darkorchid = [153,50,204]
#         mediumorchid = [186,85,211]
#         darkmagenta	= [139,0,139]
#         violet = [238,130,238]
#         orchid = [218,112,214]
#         plum = [221,160,221]

#         # Tons de Ciano
#         cyan = [0,255,255]
#         darkturquoise = [0,206,209]
#         turquoise = [64,224,208]
#         mediumturquoise	= [72,209,204]
#         lightseagreen = [32,178,170]
#         darkcyan = [0,139,139]
#         teal = [0,128,128]
#         aquamarine = [127,255,212]
#         mediumaquamarine = [102,205,170]
#         cadetblue = [95,158,160]

#         # Tons de Verde
#         darkslateGray =	[47,79,79]
#         mediumspringgreen = [0,250,154]
#         springgreen	= [0,255,127]
#         palegreen =	[152,251,152]
#         lightgreen = [144,238,144]
#         darkSeagreen = [143,188,143]
#         mediumseagreen = [60,179,113]
#         seagreen = [46,139,87]
#         darkgreen =	[0,100,0]
#         green = [0,128,0]
#         forestgreen	= [34,139,34]
#         limegreen = [50,205,50]
#         lime = [0,255,0]
#         lawngreen =	[124,252,0]
#         chartreuse = [127,255,0]
#         greenyellow	= [173,255,47]
#         yellowgreen	= [154,205,50]
#         olivedrab = [107,142,35]
#         darkolivegreen = [85,107,47]
#         olive = [128,128,0]

#         # Tons de Rosa
#         mediumvioletred	= [199,21,133]
#         deeppink = [255,20,147]
#         hotpink	= [255,105,180]
#         palevioletred =	[219,112,147]
#         lightpink = [255,182,193]
#         pink = [255,192,203]
#         lightcoral = [240,128,128]
#         indianred =	[205,92,92]
#         crimson	= [220,20,60]

#         # Tons de Vermelho
#         maroon = [128,0,0]
#         darkred = [139,0,0]
#         firebrick =	[178,34,34]
#         brown =	[165,42,42]
#         salmon = [250,128,114]
#         darksalmon = [233,150,122]
#         lightsalmon	= [255,160,122]
#         coral = [255,127,80]
#         tomato = [255,99,71]
#         red	= [255,0,0]

#         # Tons de Laranja
#         orangered = [255,69,0]
#         darkorange = [255,140,0]
#         orange = [255,165,0]

#         # Tons de Amarelo
#         gold = [255,215,0]
#         yellow = [255,255,0]
#         khaki = [240,230,140]

#         # Tons de Marrom
#         darkkhaki =	[189,83,107]
#         goldenrod =	[218,165,32]
#         darkgoldenrod =	[184,134,11]
#         saddlebrown	= [139,69,19]
#         sienna = [160,82,45]
#         rosybrown = [188,143,143]
#         peru = [205,133,63]
#         chocolate = [210,105,30]
#         sandybrown = [244,164,96]
#         navajowhite = [255,222,173]
#         wheat = [245,222,179]
#         burlywood =	[222,184,135]
#         tan	= [210,180,140]

#         # Tons Pasteis
#         aliceblue = [240,248,255]
#         ghostwhite = [248,248,255]
#         snow = [255,250,250]
#         seashell = [255,245,238]
#         floralwhite = [255,250,240]
#         whitesmoke = [245,245,245]
#         beige = [245,245,220]
#         oldLace = [253,245,230]
#         ivory = [255,255,240]
#         linen =	[250,240,230]
#         cornsilk = [255,248,220]
#         antiquewhite = [250,235,215]
#         blanchedalmond = [255,235,205]
#         bisque = [255,228,196]
#         lightyellow	= [255,255,224]
#         lemonchiffon = [255,250,205]
#         lightgoldenrodyellow = [250,250,210]
#         papayawhip = [255,239,213]
#         peachpuff = [255,218,185]
#         moccasin = [255,228,181]
#         palegoldenrod =	[238,232,170]
#         mistyrose = [255,228,225]
#         lavenderblush =	[255,240,245]
#         lavender = [230,230,250]
#         thistle	= [216,191,216]
#         azure = [240,255,255]
#         lightCyan =	[224,255,255]
#         powderblue = [176,224,230]
#         paleturquoise =	[175,238,238]
#         honeydew = [240,255,240]
#         mintcream =	[245,255,250]
#

# ------------------------------------------------------------------
# Minimal call using PYGAME
# ------------------------------------------------------------------
# 
# import pygame
# from colors import Color
#
# pygame.init()
# window = pygame.display.set_mode([300, 500])
# color = Color()
# window.fill(color.red)
# loop = True
# 
# while loop:
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             self.loop = False
#     pygame.display.update()