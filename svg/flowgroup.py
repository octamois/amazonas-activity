#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright (c) 2009, Sugar Labs

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import sys
import os
import os.path
import gettext

def main():

    myname = "flowgroup"
    mystring1 = "Flow"
    mystring2 = "wait"
    mystring3 = "forever"
    mystring4 = "repeat"
    mystring5 = "if"
    mystring6 = "then"
    mystring7 = "else"
    mystring8 = "stop stack"
    mygroup = "flow"

    if len(sys.argv) != 2:
        print "Error: Usage is " + myname + ".py lang"
        return

    t = gettext.translation("org.laptop.TurtleArtActivity", "../locale", languages=[sys.argv[1]])
    _ = t.ugettext
    t.install()

    print _(mystring1)
    print _(mystring2)
    print _(mystring3)
    print _(mystring4)
    print _(mystring5)
    print _(mystring6)
    print _(mystring7)
    print _(mystring8)

    data0 = \
"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n \
<!-- Created with Inkscape (http://www.inkscape.org/) -->\n \
<svg\n \
   xmlns:svg=\"http://www.w3.org/2000/svg\"\n \
   xmlns=\"http://www.w3.org/2000/svg\"\n \
   xmlns:xlink=\"http://www.w3.org/1999/xlink\"\n \
   version=\"1.0\"\n \
   width=\"145\"\n \
   height=\"500\"\n \
   id=\"svg2\">\n \
  <defs\n \
     id=\"defs4\">\n \
    <linearGradient\n \
       id=\"linearGradient3789\">\n \
      <stop\n \
         id=\"stop3791\"\n \
         style=\"stop-color:#ffffff;stop-opacity:1\"\n \
         offset=\"0\" />\n \
      <stop\n \
         id=\"stop3793\"\n \
         style=\"stop-color:#feb00a;stop-opacity:1\"\n \
         offset=\"1\" />\n \
    </linearGradient>\n \
    <linearGradient\n \
       x1=\"80\"\n \
       y1=\"436\"\n \
       x2=\"129\"\n \
       y2=\"436\"\n \
       id=\"linearGradient4683\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"17\"\n \
       y1=\"382\"\n \
       x2=\"128\"\n \
       y2=\"382\"\n \
       id=\"linearGradient4691\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"16\"\n \
       y1=\"325\"\n \
       x2=\"129\"\n \
       y2=\"325\"\n \
       id=\"linearGradient4699\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"80\"\n \
       y1=\"287\"\n \
       x2=\"130\"\n \
       y2=\"287\"\n \
       id=\"linearGradient4708\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"15\"\n \
       y1=\"233\"\n \
       x2=\"130\"\n \
       y2=\"233\"\n \
       id=\"linearGradient4716\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"15\"\n \
       y1=\"150\"\n \
       x2=\"130\"\n \
       y2=\"150\"\n \
       id=\"linearGradient4724\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"20\"\n \
       y1=\"92\"\n \
       x2=\"125\"\n \
       y2=\"92\"\n \
       id=\"linearGradient4732\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"43\"\n \
       y1=\"51\"\n \
       x2=\"93\"\n \
       y2=\"51\"\n \
       id=\"linearGradient4740\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"80\"\n \
       y1=\"436\"\n \
       x2=\"129\"\n \
       y2=\"436\"\n \
       id=\"linearGradient2502\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       x1=\"0\"\n \
       y1=\"22\"\n \
       x2=\"74\"\n \
       y2=\"22\"\n \
       id=\"linearGradient3172\"\n \
       xlink:href=\"#linearGradient3166\"\n \
       gradientUnits=\"userSpaceOnUse\" />\n \
    <linearGradient\n \
       id=\"linearGradient3166\">\n \
      <stop\n \
         id=\"stop3168\"\n \
         style=\"stop-color:#ffffff;stop-opacity:1\"\n \
         offset=\"0\" />\n \
      <stop\n \
         id=\"stop3170\"\n \
         style=\"stop-color:#feb00a;stop-opacity:1\"\n \
         offset=\"1\" />\n \
    </linearGradient>\n \
    <linearGradient\n \
       x1=\"0\"\n \
       y1=\"22\"\n \
       x2=\"74\"\n \
       y2=\"22\"\n \
       id=\"linearGradient2711\"\n \
       xlink:href=\"#linearGradient3166\"\n \
       gradientUnits=\"userSpaceOnUse\"\n \
       gradientTransform=\"matrix(0.67,0,0,0.67,80.04495,411.22166)\" />\n \
    <linearGradient\n \
       x1=\"80\"\n \
       y1=\"436\"\n \
       x2=\"129\"\n \
       y2=\"436\"\n \
       id=\"linearGradient3490\"\n \
       xlink:href=\"#linearGradient3789\"\n \
       gradientUnits=\"userSpaceOnUse\"\n \
       gradientTransform=\"translate(-62.75315,0)\" />\n \
  </defs>\n \
  <path\n \
     d=\"M 0.5,0.5 L 0.5,486.5 L 3.5,493 L 8.5,497 L 15,499.5 L 129,499.5 L 136,497 L 142,492 L 144.5,484 L 144.5,0.5 L 0.5,0.5 z\"\n \
     id=\"path17\"\n \
     style=\"fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1px;stroke-linejoin:miter;stroke-opacity:1\" />\n \
  <rect\n \
     width=\"137.5\"\n \
     height=\"0.14\"\n \
     x=\"4\"\n \
     y=\"-29\"\n \
     transform=\"scale(1,-1)\"\n \
     id=\"rect19\"\n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1px;stroke-opacity:1\" />\n \
  <rect\n \
     width=\"137.5\"\n \
     height=\"0.14\"\n \
     x=\"4\"\n \
     y=\"-28\"\n \
     transform=\"scale(1,-1)\"\n \
     id=\"rect21\"\n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1px;stroke-opacity:1\" />\n \
  <rect\n \
     width=\"137.5\"\n \
     height=\"0.14\"\n \
     x=\"4\"\n \
     y=\"-473\"\n \
     transform=\"scale(1,-1)\"\n \
     id=\"rect23\"\n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1px;stroke-opacity:1\" />\n \
  <rect\n \
     width=\"137.5\"\n \
     height=\"0.14\"\n \
     x=\"4\"\n \
     y=\"-471.5\"\n \
     transform=\"scale(1,-1)\"\n \
     id=\"rect25\"\n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1px;stroke-opacity:1\" />\n \
  <path\n \
     d=\"M 79.5,438.375 C 79.5,442.86231 75.750385,446.5 71.125,446.5 C 66.499615,446.5 62.75,442.86231 62.75,438.375 C 62.75,433.88769 66.499615,430.25 71.125,430.25 C 75.750385,430.25 79.5,433.88769 79.5,438.375 L 79.5,438.375 z\"\n \
     transform=\"translate(1.375,47.250977)\"\n \
     id=\"path27\"\n \
     style=\"fill:#ff4040;fill-opacity:1;stroke:#ff4040;stroke-width:1px;stroke-opacity:1\" />\n \
  <text\n \
     id=\"text29\"\n \
     style=\"font-size:12px;font-weight:bold;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"68\"\n \
       y=\"490\"\n \
       id=\"tspan31\"\n \
       style=\"font-size:12px;font-weight:bold;fill:#ffffff\">X</tspan>\n \
  </text>\n \
  <text\n \
     id=\"text33\"\n \
     style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"72.5\"\n \
       y=\"21.5\"\n \
       id=\"tspan35\"\n \
       style=\"font-size:20px\">"

    data1 = \
"</tspan>\n \
  </text>\n \
  <rect\n \
     width=\"137.5\"\n \
     height=\"0.14\"\n \
     x=\"4\"\n \
     y=\"358\"\n \
     id=\"rect37\"\n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1px;stroke-opacity:1\" />\n \
  <rect\n \
     width=\"137.5\"\n \
     height=\"0.14\"\n \
     x=\"4\"\n \
     y=\"359\"\n \
     id=\"rect39\"\n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1px;stroke-opacity:1\" />\n \
  <rect\n \
     width=\"137.5\"\n \
     height=\"0.14\"\n \
     x=\"4\"\n \
     y=\"360\"\n \
     id=\"rect41\"\n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#ffffc4;stroke-width:1px;stroke-opacity:1\" />\n \
  <path\n \
     d=\"M 90,40.3 L 101,40.3 L 101,44.3 L 98.4,44.3 L 98.4,42.3 L 91.4,42.3\"\n \
     id=\"path43\"\n \
     style=\"fill:#c18516;fill-opacity:1;stroke:#966711;stroke-width:1px;stroke-opacity:1\" />\n \
  <path\n \
     d=\"M 90,58.7 L 101,58.7 L 101,54.7 L 98.4,54.7 L 98.4,56.7 L 91.4,56.7\"\n \
     id=\"path45\"\n \
     style=\"fill:#c18516;fill-opacity:1;stroke:#966711;stroke-width:1px;stroke-opacity:1\" />\n \
  <path\n \
     d=\"M 75.416813,36.999284 C 86.084013,36.999284 86.084013,36.999284 86.084013,36.999284 C 86.084013,36.999284 88.838683,38.657069 89.750863,39.666084 C 90.682558,40.696685 92.084313,43.666284 92.084313,43.666284 L 92.084313,56.333584 C 92.084313,56.333584 90.606206,58.796143 89.750863,59.667084 C 88.797775,60.637552 86.084013,62.333884 86.084013,62.333884 L 74.750113,62.333884 L 74.750113,62.333884 L 74.750113,65.000684 L 61.416113,65.000684 L 61.416113,62.333884 L 50.082213,62.333884 C 50.082213,62.333884 47.368451,60.637552 46.415363,59.667084 C 45.56002,58.796143 44.081913,56.333584 44.081913,56.333584 L 44.081913,43.666284 C 44.081913,43.666284 45.483669,40.696685 46.415363,39.666084 C 47.327543,38.657069 50.082213,36.999284 50.082213,36.999284 L 60.749413,36.999284 L 60.749413,40.332784 L 75.416813,40.332784 L 75.416813,36.999284 z\"\n \
     id=\"path47\"\n \
     style=\"fill:url(#linearGradient4740);fill-opacity:1;stroke:#a97513;stroke-width:1px;stroke-opacity:1\" />\n \
  <text\n \
     id=\"text49\"\n \
     style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"67\"\n \
       y=\"54\"\n \
       id=\"tspan51\"\n \
       style=\"font-size:11px\">"

    data2 = \
"</tspan>\n \
  </text>\n \
  <path\n \
     d=\"M 52.50651,77.818218 C 63.17371,77.818218 63.236319,77.818218 63.236319,77.818218 C 63.236319,77.818218 65.173229,78.495457 65.838818,79.045014 C 66.44769,79.547741 67.391349,81.170331 67.391349,81.170331 L 123.84341,81.485068 L 123.891,89.240796 L 121.55099,89.2381 C 121.55099,89.2381 120.29757,87.789652 119.64925,87.294528 C 118.9423,86.754631 117.0588,85.851826 117.0588,85.851826 L 105.88312,86.028865 L 105.85182,89.211131 L 93.048297,89.262953 L 92.954386,85.746068 L 79.649998,85.985716 C 79.649998,85.985716 77.028777,87.559278 76.112597,88.479284 C 75.129121,89.466868 73.451719,92.287639 73.451719,92.287639 L 73.367112,105.89746 L 27.52283,105.95509 C 27.52283,105.95509 24.391708,104.59925 23.310266,103.57044 C 22.452508,102.75442 21.109001,100.23897 21.109001,100.23897 L 21.17161,84.485218 C 21.17161,84.485218 22.573366,81.515619 23.50506,80.485018 C 24.41724,79.476003 27.17191,77.818218 27.17191,77.818218 L 37.83911,77.818218 L 37.83911,81.151718 L 52.50651,81.151718 L 52.50651,77.818218 z\"\n \
     id=\"path53\"\n \
     style=\"fill:url(#linearGradient4732);fill-opacity:1;stroke:#a97513;stroke-width:1px;stroke-opacity:1\" />\n "

    data2a = \
"  <text\n \
     id=\"text55\"\n \
     style=\"font-size:11px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"47\"\n \
       y=\"96\"\n \
       id=\"tspan57\"\n \
       style=\"font-size:11px\">"

    data2b = \
"  <text\n \
     id=\"text55\"\n \
     style=\"font-size:11px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"47\"\n \
       y=\"90\"\n \
       id=\"tspan57\"\n \
       style=\"font-size:11px\">"

    data2c = \
"</tspan>\n \
  </text>\n \
  <text\n \
     id=\"text55\"\n \
     style=\"font-size:11px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"47\"\n \
       y=\"102\"\n \
       id=\"tspan57\"\n \
       style=\"font-size:11px\">"

    data3 = \
"</tspan>\n \
  </text>\n \
  <path\n \
     d=\"M 47.49875,118.77264 C 58.16595,118.77264 58.291168,118.77264 58.291168,118.77264 C 58.291168,118.77264 60.228077,119.31441 60.893666,119.86396 C 61.502538,120.36669 62.547725,121.70003 62.547725,121.70003 L 80.83375,121.90308 L 80.83375,125.43964 L 77.845874,125.43964 L 77.676031,123.43954 L 72.16665,123.43954 L 72.16665,138.77364 L 77.707364,138.77364 L 77.74058,136.77354 L 80.83375,136.77354 L 80.83375,145.44064 L 128.83615,145.44064 L 128.83615,153.44104 L 125.2357,153.38351 C 125.2357,153.38351 124.38839,151.78404 123.74008,151.28892 C 123.03313,150.74902 121.50245,150.10754 121.50245,150.10754 L 110.16855,150.10754 L 110.16855,153.44104 L 96.83455,153.44104 L 96.83455,150.10754 L 84.16725,150.10754 C 84.16725,150.10754 81.729429,151.67768 80.914125,152.47367 C 79.925757,153.43864 78.16695,155.67286 78.16695,155.67286 L 78.16695,172.10864 L 65.635735,172.04467 C 65.635735,172.04467 64.327685,175.04114 63.35715,176.01146 C 62.402334,176.96607 59.454117,178.10894 59.454117,178.10894 L 46.83205,178.10894 L 46.83205,180.77574 L 34.16475,180.77574 L 34.16475,178.10894 L 22.780735,178.10894 C 22.780735,178.10894 19.649613,176.83094 18.568171,175.80212 C 17.710413,174.98611 16.16385,172.47065 16.16385,172.47065 L 16.16385,125.30417 C 16.16385,125.30417 17.628215,122.33457 18.559909,121.30397 C 19.472089,120.29495 22.226759,118.77264 22.226759,118.77264 L 32.83135,118.77264 L 32.83135,122.10614 L 47.49875,122.10614 L 47.49875,118.77264 z\"\n \
     id=\"path59\"\n \
     style=\"fill:url(#linearGradient4724);fill-opacity:1;stroke:#a97513;stroke-width:1px;stroke-opacity:1\" />\n \
  <text\n \
     id=\"text61\"\n \
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"44\"\n \
       y=\"136\"\n \
       id=\"tspan63\"\n \
       style=\"font-size:11px\">"

    data4 = \
"</tspan>\n \
  </text>\n \
  <path\n \
     d=\"M 47.49875,193.59327 C 58.16595,193.59327 58.291168,193.59327 58.291168,193.59327 C 58.291168,193.59327 60.228077,194.13504 60.893666,194.68459 C 61.502538,195.18732 62.446197,196.92677 62.446197,196.92677 L 88.16745,196.92677 L 88.16745,199.83541 C 88.16745,199.83541 79.457707,200.90587 76.322955,202.6477 C 73.623788,204.1475 69.9625,206.54556 68.741575,209.31806 C 67.910373,211.20556 68.002913,214.32311 68.876317,216.19147 C 69.992727,218.57965 73.182145,220.71515 75.506966,221.95813 C 78.856423,223.74893 88.16745,225.28812 88.16745,225.28812 L 88.16745,229.59507 L 124.23283,229.59507 L 127.00542,231.82614 L 128.83615,234.75002 L 128.83615,244.92917 L 125.64182,244.92917 C 125.64182,244.92917 124.79451,243.3297 124.14619,242.83458 C 123.43924,242.29468 121.50245,241.59567 121.50245,241.59567 L 110.16855,241.59567 L 110.16855,244.92917 L 96.83455,244.92917 L 96.83455,241.59567 L 84.16725,241.59567 C 84.16725,241.59567 81.323318,243.12181 80.508014,243.91781 C 79.519645,244.88277 78.16695,247.82769 78.16695,247.82769 L 78.16695,262.93007 L 65.635735,262.8661 C 65.635735,262.8661 64.327685,265.86257 63.35715,266.83289 C 62.402334,267.7875 59.454117,269.07371 59.454117,269.07371 L 46.83205,268.93037 L 46.83205,272.26387 L 34.16475,272.26387 L 34.16475,268.93037 L 22.780735,268.93037 C 22.780735,268.93037 19.649613,267.65237 18.568171,266.62355 C 17.710413,265.80754 16.16385,263.29208 16.16385,263.29208 L 16.16385,200.1248 C 16.16385,200.1248 17.628215,197.1552 18.559909,196.1246 C 19.472089,195.11558 22.226759,193.59327 22.226759,193.59327 L 32.83135,193.59327 L 32.83135,196.92677 L 47.49875,196.92677 L 47.49875,193.59327 z\"\n \
     id=\"path65\"\n \
     style=\"fill:url(#linearGradient4716);fill-opacity:1;stroke:#a97513;stroke-width:1px;stroke-opacity:1\" />\n \
  <text\n \
     id=\"text67\"\n \
     style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"39\"\n \
       y=\"212\"\n \
       id=\"tspan69\"\n \
       style=\"font-size:11px\">"

    data5 = \
"</tspan>\n \
  </text>\n \
  <text\n \
     id=\"text71\"\n \
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"103\"\n \
       y=\"238.5\"\n \
       id=\"tspan73\"\n \
       style=\"font-size:9px\">"

    data6 = \
"</tspan>\n \
  </text>\n \
  <path\n \
     d=\"M 112.16865,271.51111 C 122.83585,271.51111 122.83585,271.51111 122.83585,271.51111 C 122.83585,271.51111 125.59052,273.16889 126.5027,274.17791 C 127.43439,275.20851 128.83615,278.17811 128.83615,278.17811 L 128.83615,290.17871 L 105.1683,302.84601 C 105.1683,302.84601 80.83375,290.17871 80.83375,290.17871 L 80.83375,278.17811 C 80.83375,278.17811 82.235506,275.20851 83.1672,274.17791 C 84.07938,273.16889 86.83405,271.51111 86.83405,271.51111 L 97.50125,271.51111 L 97.50125,274.84461 L 112.16865,274.84461 L 112.16865,271.51111 z\"\n \
     id=\"path75\"\n \
     style=\"fill:url(#linearGradient4708);fill-opacity:1;stroke:#a97513;stroke-width:1px;stroke-opacity:1\" />\n \
  <text\n \
     id=\"text77\"\n \
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"105\"\n \
       y=\"283\"\n \
       id=\"tspan79\"\n \
       style=\"font-size:10px\">"

    data7 = \
"</tspan>\n \
  </text>\n \
  <text\n \
     id=\"text81\"\n \
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"105\"\n \
       y=\"294\"\n \
       id=\"tspan83\"\n \
       style=\"font-size:10px\">"

    data8 = \
"</tspan>\n \
  </text>\n \
  <path\n \
     d=\"M 36.940888,299.20373 C 44.052711,299.20373 44.136193,299.20373 44.136193,299.20373 C 44.136193,299.20373 45.427531,299.56492 45.871279,299.93131 C 46.277214,300.26648 46.906352,301.42617 46.906352,301.42617 L 64.054711,301.42617 L 64.054711,303.36536 C 64.054711,303.36536 58.247925,304.07904 56.157986,305.24032 C 54.358452,306.24023 51.917471,307.83902 51.10348,309.68744 C 50.549318,310.94584 50.611014,313.02432 51.193312,314.26995 C 51.937623,315.86215 54.064008,317.28588 55.613966,318.11458 C 57.847049,319.30851 64.054711,320.33468 64.054711,320.33468 L 64.054711,323.20613 L 125.93746,323.20613 L 127.78595,324.62589 L 128.95009,326.57524 L 128.95009,333.42937 L 126.87683,333.42937 C 126.87683,333.42937 126.31193,332.29532 125.8797,331.96522 C 125.40838,331.60527 124.11712,331.20693 124.11712,331.20693 L 116.5044,331.20693 L 116.5044,333.42937 L 108.05911,333.42937 L 108.05911,331.20693 L 99.603951,331.20693 C 99.603951,331.20693 97.505568,331.91803 96.848529,332.55436 C 96.068482,333.30981 96.00968,333.27413 95.24339,334.62327 L 95.011478,345.61026 L 90.279556,345.43424 L 90.279556,334.30933 C 90.279556,334.30933 89.296987,333.10246 88.853018,332.67916 C 88.350421,332.19995 86.969296,331.20693 86.969296,331.20693 L 78.722845,331.20693 L 78.722845,333.42937 L 70.277556,333.42937 L 70.277556,331.20693 L 61.387778,331.20693 C 61.387778,331.20693 59.491728,332.22441 58.948165,332.7551 C 58.289219,333.39844 57.387378,335.36182 57.387378,335.36182 L 57.387378,345.43057 L 49.032817,345.38793 C 49.032817,345.38793 48.160739,347.38567 47.513683,348.03259 C 46.877108,348.66902 44.911532,349.52654 44.911532,349.52654 L 36.496399,349.43097 L 36.496399,351.65342 L 28.05111,351.65342 L 28.05111,349.43097 L 20.461387,349.43097 C 20.461387,349.43097 18.373868,348.57893 17.652871,347.89302 C 17.081003,347.34898 16.04991,345.67193 16.04991,345.67193 L 16.04991,303.5583 C 16.04991,303.5583 17.026202,301.57847 17.647362,300.89136 C 18.255513,300.21865 20.092052,299.20373 20.092052,299.20373 L 27.162132,299.20373 L 27.162132,301.42617 L 36.940888,301.42617 L 36.940888,299.20373 z\"\n \
     id=\"path85\"\n \
     style=\"fill:url(#linearGradient4699);fill-opacity:1;stroke:#a97513;stroke-width:1px;stroke-opacity:1\" />\n \
  <text\n \
     id=\"text87\"\n \
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"32\"\n \
       y=\"314\"\n \
       id=\"tspan89\"\n \
       style=\"font-size:11px\">"

    data9 = \
"</tspan>\n \
  </text>\n \
  <text\n \
     id=\"text91\"\n \
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"74\"\n \
       y=\"329\"\n \
       id=\"tspan93\"\n \
       style=\"font-size:6px\">"

    data10 = \
"</tspan>\n \
  </text>\n \
  <text\n \
     id=\"text95\"\n \
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\n \
    <tspan\n \
       x=\"111\"\n \
       y=\"329\"\n \
       id=\"tspan97\"\n \
       style=\"font-size:6px\">"

    data11 = \
"</tspan>\n \
  </text>\n \
  <path\n \
     d=\"M 49.8322,372.80906 C 60.4994,372.80906 59.49935,372.80906 59.49935,372.80906 C 59.49935,372.80906 61.567081,373.4166 62.232671,373.96615 C 62.841543,374.46888 63.8329,376.14256 63.8329,376.14256 L 67.8331,376.14256 L 67.8331,366.80876 L 127.1694,366.80876 L 127.1694,374.14246 L 124.83595,374.14246 C 124.83595,374.14246 123.50523,372.7019 122.8201,372.15446 C 122.01247,371.50913 119.8357,370.80896 119.8357,370.80896 L 109.1685,370.80896 L 109.1685,374.14246 L 96.5012,374.14246 L 96.5012,370.80896 L 83.8339,370.80896 C 83.8339,370.80896 80.63569,372.47259 79.813801,373.30588 C 78.826981,374.30638 77.1669,377.47596 77.1669,377.47596 L 77.1669,397.47696 L 24.4976,397.47696 C 24.4976,397.47696 21.021359,396.46106 19.973726,395.53967 C 18.833507,394.53684 17.8306,391.47666 17.8306,391.47666 L 17.8306,378.50052 C 17.8306,378.50052 19.191494,375.74876 19.968592,374.98808 C 20.940621,374.03658 23.8309,372.80906 23.8309,372.80906 L 34.4981,372.80906 L 34.4981,376.14256 L 49.8322,376.14256 L 49.8322,372.80906 z\"\n \
     id=\"path99\"\n \
     style=\"fill:url(#linearGradient4691);fill-opacity:1;stroke:#a97513;stroke-width:1px;stroke-opacity:1\" />\n \
  <path\n \
     d=\"M 49.4155,411.64166 C 60.0827,411.64166 60.0827,411.64166 60.0827,411.64166 C 60.0827,411.64166 62.83737,413.29944 63.74955,414.30846 C 64.68124,415.33906 66.083,418.30866 66.083,418.30866 L 66.083,450.97696 C 66.083,450.97696 64.60489,453.43952 63.74955,454.31046 C 62.79646,455.28093 60.0827,456.97726 60.0827,456.97726 L 48.7488,456.97726 L 48.7488,456.97726 L 48.7488,459.64406 L 35.4148,459.64406 L 35.4148,456.97726 L 24.0809,456.97726 C 24.0809,456.97726 21.367138,455.28093 20.41405,454.31046 C 19.558707,453.43952 18.0806,450.97696 18.0806,450.97696 L 18.0806,418.30866 C 18.0806,418.30866 19.482356,415.33906 20.41405,414.30846 C 21.32623,413.29944 24.0809,411.64166 24.0809,411.64166 L 34.7481,411.64166 L 34.7481,414.97516 L 49.4155,414.97516 L 49.4155,411.64166 z\"\n \
     id=\"path109\"\n \
     style=\"fill:url(#linearGradient3490);fill-opacity:1;stroke:#a97513;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" />\n \
  <path\n \
     d=\"M 112.20495,411.89166 C 122.92495,411.89166 122.92495,411.89166 122.92495,411.89166 C 122.92495,411.89166 125.69325,413.55765 126.60995,414.57166 C 127.54626,415.60736 128.95495,418.59166 128.95495,418.59166 L 128.95495,431.32166 C 128.95495,431.32166 127.46953,433.79641 126.60995,434.67166 C 125.65214,435.64693 122.92495,437.35166 122.92495,437.35166 L 111.53495,437.35166 L 111.53495,437.35166 L 111.53495,440.03166 L 98.13495,440.03166 L 98.13495,437.35166 L 86.74495,437.35166 C 86.74495,437.35166 84.017756,435.64693 83.05995,434.67166 C 82.200373,433.79641 80.71495,431.32166 80.71495,431.32166 L 80.71495,418.59166 C 80.71495,418.59166 82.123644,415.60736 83.05995,414.57166 C 83.976645,413.55765 86.74495,411.89166 86.74495,411.89166 L 97.46495,411.89166 L 97.46495,415.24166 L 112.20495,415.24166 L 112.20495,411.89166 z\"\n \
     id=\"path14\"\n \
     style=\"fill:url(#linearGradient2711);fill-opacity:1;stroke:#a97513;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" />\n \
  <rect\n \
     width=\"11.94208\"\n \
     height=\"9.4202003\"\n \
     x=\"98.863907\"\n \
     y=\"424.68732\"\n \
     id=\"rect2483\"\n \
     style=\"fill:#666666;stroke-width:2;stroke-miterlimit:4;stroke-dasharray:none\" />\n \
  <path\n \
     d=\"M 101.49433,424.68732 L 101.49433,422.25053 C 101.49433,420.44689 102.95493,418.9883 104.75589,418.9883 C 106.55685,418.9883 108.01678,420.44957 108.01678,422.25053 L 108.01678,424.68732\"\n \
     id=\"path2485\"\n \
     style=\"fill:none;stroke:#666666;stroke-width:2;stroke-miterlimit:4;stroke-dasharray:none\" />\n \
</svg>\n"

    FILE = open(os.path.join("../images", sys.argv[1], mygroup, myname+".svg"), "w")
    FILE.write(data0)
    FILE.write(_(mystring1).encode("utf-8"))
    FILE.write(data1)
    FILE.write(_(mystring2).encode("utf-8"))
    FILE.write(data2)
    strings = _(mystring3).split(" ",2)
    if len(strings) == 1:
        FILE.write(data2a)
        FILE.write(strings[0].encode("utf-8"))
    else:
        FILE.write(data2b)
        FILE.write(strings[0].encode("utf-8"))
        FILE.write(data2c)
        FILE.write(strings[1].encode("utf-8"))
    FILE.write(data3)
    FILE.write(_(mystring4).encode("utf-8"))
    FILE.write(data4)
    FILE.write(_(mystring5).encode("utf-8"))
    FILE.write(data5)
    FILE.write(_(mystring6).encode("utf-8"))
    FILE.write(data6)
    strings = _(mystring8).split(" ",2)
    FILE.write(strings[0].encode("utf-8"))
    FILE.write(data7)
    if len(strings) == 2:
        FILE.write(strings[1].encode("utf-8"))
    FILE.write(data8)
    FILE.write(_(mystring5).encode("utf-8"))
    FILE.write(data9)
    FILE.write(_(mystring6).encode("utf-8"))
    FILE.write(data10)
    FILE.write(_(mystring7).encode("utf-8"))
    FILE.write(data11)
    FILE.close()
    return

if __name__ == "__main__":
    main()
