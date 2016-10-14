<?xml version="1.0" encoding="ascii"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
<head>
<link rel="icon" href="/FS/orbweaver/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow"/>
<link rel="stylesheet" href="/FS/orbweaver/static/style-gitweb.css" type="text/css" />
<script type="text/javascript" src="/FS/orbweaver/static/mercurial.js"></script>

<title>FS/orbweaver: orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py@07f9e9bfecab</title>
<link rel="alternate" type="application/atom+xml"
   href="/FS/orbweaver/atom-log" title="Atom feed for FS/orbweaver"/>
<link rel="alternate" type="application/rss+xml"
   href="/FS/orbweaver/rss-log" title="RSS feed for FS/orbweaver"/>
</head>
<body>

<div class="page_header">
<a href="http://mercurial.selenic.com/" title="Mercurial" style="float: right;">Mercurial</a><a href="/FS/orbweaver/summary">FS/orbweaver</a> / file revision
</div>

<div class="page_nav">
<a href="/FS/orbweaver/summary">summary</a> |
<a href="/FS/orbweaver/shortlog">shortlog</a> |
<a href="/FS/orbweaver/log">changelog</a> |
<a href="/FS/orbweaver/graph">graph</a> |
<a href="/FS/orbweaver/tags">tags</a> |
<a href="/FS/orbweaver/bookmarks">bookmarks</a> |
<a href="/FS/orbweaver/branches">branches</a> |
<a href="/FS/orbweaver/file/07f9e9bfecab/orbweaver-signal_distance_map_generator/src/sdm_simulator/">files</a> |
<a href="/FS/orbweaver/rev/07f9e9bfecab">changeset</a> |
file |
<a href="/FS/orbweaver/file/tip/orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py">latest</a> |
<a href="/FS/orbweaver/log/07f9e9bfecab/orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py">revisions</a> |
<a href="/FS/orbweaver/annotate/07f9e9bfecab/orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py">annotate</a> |
<a href="/FS/orbweaver/diff/07f9e9bfecab/orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py">diff</a> |
<a href="/FS/orbweaver/raw-file/07f9e9bfecab/orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py">raw</a> |
<a href="/FS/orbweaver/help">help</a>
<br/>
</div>

<div class="title">orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py</div>

<div class="title_text">
<table cellspacing="0">
<tr>
 <td>author</td>
 <td>&#66;&#114;&#97;&#110;&#100;&#111;&#110;&#32;&#80;&#46;&#32;&#69;&#110;&#111;&#99;&#104;&#115;&#32;&#60;&#98;&#114;&#97;&#110;&#100;&#111;&#110;&#46;&#101;&#110;&#111;&#99;&#104;&#115;&#64;&#110;&#114;&#108;&#46;&#110;&#97;&#118;&#121;&#46;&#109;&#105;&#108;&#62;</td></tr>
<tr>
 <td></td>
 <td class="date age">Fri, 14 Oct 2016 09:40:31 -0400</td></tr>

<tr>
 <td>changeset 681</td>
 <td style="font-family:monospace"><a class="list" href="/FS/orbweaver/rev/07f9e9bfecab">07f9e9bfecab</a></td></tr>

<tr>
<td>parent 529</td>
<td style="font-family:monospace">
<a class="list" href="/FS/orbweaver/file/09cf38de2f73/orbweaver-signal_distance_map_generator/src/sdm_simulator/kml_utilities.py">
09cf38de2f73
</a>
</td>
</tr>

<tr>
 <td>permissions</td>
 <td style="font-family:monospace">-rw-r--r--</td></tr>
</table>
</div>

<div class="page_path">
FLYINGSQUIRREL-1738: fixed an ArrayIndexOutOfBoundsException in SdmGeolocationStrategyImplementation.  It assumed that it was always using 3D geolocation.<br/>
<br/>
+review FLYINGSQUIRREL-400
</div>

<div class="page_body">

<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l1" id="l1">     1</a> import math
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l2" id="l2">     2</a> import jet_color_map
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l3" id="l3">     3</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l4" id="l4">     4</a> ALTITUDE = 400
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l5" id="l5">     5</a> RANGE = 400
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l6" id="l6">     6</a> DRIVE_PATH_WIDTH = 3
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l7" id="l7">     7</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l8" id="l8">     8</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l9" id="l9">     9</a> def create_tour_open(foldername):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l10" id="l10">    10</a>     XMLVERSION = &quot;&lt;?xml version=\&quot;1.0\&quot; encoding=\&quot;UTF-8\&quot;?&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l11" id="l11">    11</a>     KMLXMLNS = &quot;&lt;kml xmlns=\&quot;http://www.opengis.net/kml/2.2\&quot; xmlns:gx=\&quot;http://www.google.com/kml/ext/2.2\&quot; &quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l12" id="l12">    12</a>                &quot;xmlns:kml=\&quot;http://www.opengis.net/kml/2.2\&quot; xmlns:atom=\&quot;http://www.w3.org/2005/Atom\&quot;&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l13" id="l13">    13</a>     DOCUMENT_NAME = &quot;\t&lt;Document&gt;\n&quot; + \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l14" id="l14">    14</a>                     &quot;\t\t&lt;name&gt;{}&lt;/name&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l15" id="l15">    15</a>                     &quot;\t\t&lt;open&gt;1&lt;/open&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l16" id="l16">    16</a>                     &quot;\t\t&lt;visibility&gt;1&lt;/visibility&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l17" id="l17">    17</a>     return XMLVERSION + KMLXMLNS + DOCUMENT_NAME.format(foldername)
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l18" id="l18">    18</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l19" id="l19">    19</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l20" id="l20">    20</a> def create_tour_close():
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l21" id="l21">    21</a>     return &quot;\t&lt;/Document&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l22" id="l22">    22</a>            &quot;&lt;/kml&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l23" id="l23">    23</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l24" id="l24">    24</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l25" id="l25">    25</a> def create_icon(icon, icon_name, scale=1, heading=None):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l26" id="l26">    26</a>     output = &quot;\t\t&lt;Style id=\&quot;&quot; + icon_name + &quot;\&quot;&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l27" id="l27">    27</a>                                               &quot;\t\t\t&lt;IconStyle&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l28" id="l28">    28</a>                                               &quot;\t\t\t\t&lt;scale&gt;&quot; + repr(scale) + &quot;&lt;/scale&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l29" id="l29">    29</a>     if heading is not None:
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l30" id="l30">    30</a>         output += &quot;\t\t\t\t&lt;heading&gt;&quot; + repr(heading) + &quot;&lt;/heading&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l31" id="l31">    31</a>     output += &quot;\t   \t\t\t&lt;Icon&gt;&lt;href&gt;&quot; + icon + &quot;&lt;/href&gt;&lt;/Icon&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l32" id="l32">    32</a>                                                  &quot;\t\t\t&lt;/IconStyle&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l33" id="l33">    33</a>                                                  &quot;\t\t&lt;/Style&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l34" id="l34">    34</a>     return output
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l35" id="l35">    35</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l36" id="l36">    36</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l37" id="l37">    37</a> def create_initial_view(point):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l38" id="l38">    38</a>     return &quot;\t\t&lt;LookAt&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l39" id="l39">    39</a>            &quot;\t\t\t&lt;longitude&gt;&quot; + repr(point.longitude) + &quot;&lt;/longitude&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l40" id="l40">    40</a>                                                          &quot;&lt;latitude&gt;&quot; + repr(point.latitude) + &quot;&lt;/latitude&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l41" id="l41">    41</a>                                                                                                &quot;&lt;altitude&gt;&quot; + repr(
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l42" id="l42">    42</a>         ALTITUDE) + &quot;&lt;/altitude&gt;&lt;tilt&gt;0&lt;/tilt&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l43" id="l43">    43</a>                     &quot;&lt;range&gt;&quot; + repr(RANGE) + &quot;&lt;/range&gt;&lt;heading&gt;0&lt;/heading&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l44" id="l44">    44</a>                                               &quot;\t\t&lt;/LookAt&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l45" id="l45">    45</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l46" id="l46">    46</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l47" id="l47">    47</a> def create_initial_view(point, heading, tilt=0):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l48" id="l48">    48</a>     return &quot;\t\t&lt;LookAt&gt;\n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l49" id="l49">    49</a>            \t\t\t&lt;longitude&gt;{0}&lt;/longitude&gt;\n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l50" id="l50">    50</a>            \t\t\t&lt;latitude&gt;{1}&lt;/latitude&gt;\n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l51" id="l51">    51</a>            \t\t\t&lt;altitude&gt;{2}&lt;/altitude&gt;&lt;tilt&gt;0&lt;/tilt&gt;\n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l52" id="l52">    52</a>            \t\t\t&lt;range&gt;{3}&lt;/range&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l53" id="l53">    53</a>            \t\t\t&lt;heading&gt;{4}&lt;/heading&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l54" id="l54">    54</a>             \t\t\t&lt;tilt&gt;{5}&lt;/tilt&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l55" id="l55">    55</a>            \t\t&lt;/LookAt&gt;\n&quot;.format(point.longitude,
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l56" id="l56">    56</a>                                    point.latitude,
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l57" id="l57">    57</a>                                    point.altitude,
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l58" id="l58">    58</a>                                    RANGE,
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l59" id="l59">    59</a>                                    heading,
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l60" id="l60">    60</a>                                    tilt)
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l61" id="l61">    61</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l62" id="l62">    62</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l63" id="l63">    63</a> def create_screen_overlay(icon, iconName, x_position, y_position):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l64" id="l64">    64</a>     return &quot;\t\t&lt;ScreenOverlay id=\&quot;aplegend\&quot;&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l65" id="l65">    65</a>            &quot;\t\t\t&lt;name&gt;&lt;/name&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l66" id="l66">    66</a>            &quot;\t\t\t&lt;Icon&gt;&lt;href&gt;&quot; + icon + &quot;&lt;/href&gt;&lt;/Icon&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l67" id="l67">    67</a>                                          &quot;\t\t\t&lt;overlayXY x=\&quot;&quot; + repr(x_position) + &quot;\&quot; y=\&quot;&quot; + repr(y_position) + \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l68" id="l68">    68</a>            &quot;\&quot; xunits=\&quot;fraction\&quot; yunits=\&quot;fraction\&quot;/&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l69" id="l69">    69</a>            &quot;\t\t\t&lt;screenXY x=\&quot;&quot; + repr(x_position) + &quot;\&quot; y=\&quot;&quot; + repr(y_position) + \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l70" id="l70">    70</a>            &quot;\&quot; xunits=\&quot;fraction\&quot; yunits=\&quot;fraction\&quot;/&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l71" id="l71">    71</a>            &quot;\t\t&lt;/ScreenOverlay&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l72" id="l72">    72</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l73" id="l73">    73</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l74" id="l74">    74</a> def create_folder_open(folder_name):
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l75" id="l75">    75</a>     return &quot;\t\t&lt;Folder id='PlotView'&gt;\n \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l76" id="l76">    76</a>            \t\t\t&lt;name&gt;{0}&lt;/name&gt;\n \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l77" id="l77">    77</a>            \t\t\t&lt;open&gt;0&lt;/open&gt;&lt;visibility&gt;0&lt;/visibility&gt;\n&quot;.format(folder_name)
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l78" id="l78">    78</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l79" id="l79">    79</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l80" id="l80">    80</a> def create_folder_close():
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l81" id="l81">    81</a>     return &quot;\t\t&lt;/Folder&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l82" id="l82">    82</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l83" id="l83">    83</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l84" id="l84">    84</a> def plot_icon(icon, location, name):
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l85" id="l85">    85</a>     result = &quot;\t\t&lt;Placemark&gt;\n \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l86" id="l86">    86</a>                 \t\t\t&lt;name&gt;{0}&lt;/name&gt;\n \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l87" id="l87">    87</a>                 \t\t\t&lt;styleUrl&gt;#{1}&lt;/styleUrl&gt;\n \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l88" id="l88">    88</a>                 \t\t\t&lt;open&gt;0&lt;/open&gt;&lt;visibility&gt;0&lt;/visibility&gt;\n \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l89" id="l89">    89</a>                 \t\t\t&lt;Point&gt;&quot;.format(name, icon)
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l90" id="l90">    90</a>     if location.altitude != 0:
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l91" id="l91">    91</a>         result += &quot;&lt;altitudeMode&gt;absolute&lt;/altitudeMode&gt;&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l92" id="l92">    92</a>     result += &quot;&lt;coordinates&gt;{0},{1},{2}&lt;/coordinates&gt;&lt;/Point&gt;\n \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l93" id="l93">    93</a>                 \t\t&lt;/Placemark&gt;\n&quot;.format(location.longitude, location.latitude, location.altitude)
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l94" id="l94">    94</a>     return result
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l95" id="l95">    95</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l96" id="l96">    96</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l97" id="l97">    97</a> def plot_line(name, line_color, line_width, start_point, end_point):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l98" id="l98">    98</a>     return &quot;\t\t\t&lt;Placemark&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l99" id="l99">    99</a>             \t\t\t\t&lt;name&gt;{0}&lt;/name&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l100" id="l100">   100</a>             \t\t\t\t&lt;visibility&gt;0&lt;/visibility&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l101" id="l101">   101</a>             \t\t\t\t&lt;Style id=\&quot;linestyleExample\&quot;&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l102" id="l102">   102</a>             \t\t\t\t&lt;LineStyle&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l103" id="l103">   103</a>             \t\t\t\t\t&lt;color&gt;{1}&lt;/color&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l104" id="l104">   104</a>             \t\t\t\t\t&lt;width&gt;{2}&lt;/width&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l105" id="l105">   105</a>             \t\t\t\t&lt;/LineStyle&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l106" id="l106">   106</a>             \t\t\t\t&lt;/Style&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l107" id="l107">   107</a>             \t\t\t\t&lt;LineString&gt;&lt;altitudeMode&gt;absolute&lt;/altitudeMode&gt;&lt;coordinates&gt;{3},{4},{5},{6},{7},{8}&lt;/coordinates&gt;&lt;/LineString&gt; \n\
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l108" id="l108">   108</a>             \t\t\t&lt;/Placemark&gt;\n&quot;.format(name, line_color, line_width, start_point.longitude, start_point.latitude,
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l109" id="l109">   109</a>                                          start_point.altitude, end_point.longitude, end_point.latitude,
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l110" id="l110">   110</a>                                          end_point.altitude)
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l111" id="l111">   111</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l112" id="l112">   112</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l113" id="l113">   113</a> def plot_linear_ring(border_color, polygon_color, folder_name, points):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l114" id="l114">   114</a>     result = &quot;\t\t\t&lt;Placemark&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l115" id="l115">   115</a>              &quot;\t\t\t\t&lt;name&gt;&quot; + folder_name + &quot;&lt;/name&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l116" id="l116">   116</a>                                               &quot;\t\t\t\t&lt;open&gt;0&lt;/open&gt;&lt;visibility&gt;0&lt;/visibility&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l117" id="l117">   117</a>                                               &quot;\t\t\t\t&lt;Style&gt;&lt;LineStyle&gt;&lt;color&gt;&quot; + border_color + &quot;&lt;/color&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l118" id="l118">   118</a>                                                                                                    &quot;&lt;width&gt;2&lt;/width&gt;&lt;/LineStyle&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l119" id="l119">   119</a>                                                                                                    &quot;&lt;PolyStyle&gt;&lt;color&gt;&quot; + polygon_color + &quot;&lt;/color&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l120" id="l120">   120</a>                                                                                                                                           &quot;&lt;/PolyStyle&gt;&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l121" id="l121">   121</a>                                                                                                                                           &quot;&lt;/Style&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l122" id="l122">   122</a>                                                                                                                                           &quot;\t\t\t\t\t&lt;Polygon&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l123" id="l123">   123</a>                                                                                                                                           &quot;\t\t\t\t\t\t&lt;altitudeMode&gt;relativeToGround&lt;/altitudeMode&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l124" id="l124">   124</a>                                                                                                                                           &quot;\t\t\t\t\t\t&lt;outerBoundaryIs&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l125" id="l125">   125</a>                                                                                                                                           &quot;\t\t\t\t\t\t\t&lt;LinearRing&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l126" id="l126">   126</a>                                                                                                                                           &quot;\t\t\t\t\t\t\t\t&lt;coordinates&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l127" id="l127">   127</a>     for value in points:
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l128" id="l128">   128</a>         result += &quot;\t\t\t\t\t\t\t\t&quot; + repr(value.longitude) + &quot;,&quot; + \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l129" id="l129">   129</a>                   repr(value.latitude) + &quot;,&quot; + \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l130" id="l130">   130</a>                   repr(value.altitude) + &quot;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l131" id="l131">   131</a>     result += &quot;\t\t\t\t\t\t\t\t&lt;/coordinates&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l132" id="l132">   132</a>               &quot;\t\t\t\t\t\t\t&lt;/LinearRing&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l133" id="l133">   133</a>               &quot;\t\t\t\t\t\t&lt;/outerBoundaryIs&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l134" id="l134">   134</a>               &quot;\t\t\t\t\t&lt;/Polygon&gt;\n&quot; \
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l135" id="l135">   135</a>               &quot;\t\t\t&lt;/Placemark&gt;\n&quot;
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l136" id="l136">   136</a>     return result
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l137" id="l137">   137</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l138" id="l138">   138</a> 
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l139" id="l139">   139</a> def create_color_from_extrema(opacity, value, extrema):
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l140" id="l140">   140</a>     difference = math.fabs(extrema.max - extrema.min)
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l141" id="l141">   141</a>     if difference == 0.0:
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l142" id="l142">   142</a>         return jet_color_map.create_color_string(opacity, 1.0)
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l143" id="l143">   143</a>     else:
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l144" id="l144">   144</a>         stepSize = .95 / difference
</pre>
</div>
<div style="font-family:monospace" class="parity0">
<pre><a class="linenr" href="#l145" id="l145">   145</a>         normalized_signal = 1.0 - (stepSize * math.fabs(extrema.max - value))
</pre>
</div>
<div style="font-family:monospace" class="parity1">
<pre><a class="linenr" href="#l146" id="l146">   146</a>         return jet_color_map.create_color_string(opacity, normalized_signal)
</pre>
</div>
</div>

<script type="text/javascript">process_dates()</script>
<div class="page_footer">
<div class="page_footer_text">FS/orbweaver</div>
<div class="rss_logo">
<a href="/FS/orbweaver/rss-log">RSS</a>
<a href="/FS/orbweaver/atom-log">Atom</a>
</div>
<br />

</div>
</body>
</html>

