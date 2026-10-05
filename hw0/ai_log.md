# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional):**

### Prompt 1

```
(paste your prompt)
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for [audience] who want to [goal]. My sketch is attached; follow it. Explain how the code works in plain language, section by section.

**AI's reply:**

Read a file, created a file, shared files
I built the app as a single art-explorer.html file that follows your sketch. I haven't opened it in a browser or tested a live search, so run it once to confirm results load.

Your prompt still had [audience] and [goal] as blanks. I assumed it's for curious visitors and students who want to explore the museum's collection by drawing or typing and save favorites. Tell me the real audience and goal if that's off.

Open the file in a browser on your own machine. It can't be published as a hosted page, because hosted pages block requests to api.artic.edu.

How the code works
1. Page and styles (top of the file). The layout mirrors your sketch:

A header with the title and search box.
Three tabs: Sketch Search, Text Search and My Collection.
A left sidebar of filters.
A main area with the drawing pad, the results grid and page numbers.
The CSS is small. On narrow screens the sidebar moves above the results.

2. Filters. The Art form and Subject checkboxes are built from two short lists, so adding one is a single word. ticked() reads which boxes are checked. The Year From/To fields are plain number inputs. "Drawing" is sent to the API as "Drawing and Watercolor", which is the museum's own name for that category.

3. Sketch pad. The <canvas> listens for pointer events, so it works with a mouse, finger or stylus.

Pen: draws lines and records the box that surrounds everything you've drawn.
Eraser: wipes pixels.
Clear: wipes the whole canvas.
Stroke − / = / +: thinner, default, thicker.
4. "Use sketch to search". The museum's API only searches text and can't match a picture. So the app looks at the overall shape of your drawing:

Tall and narrow becomes "portrait figure".
Very wide becomes "landscape".
Anything else becomes "still life".
It shows which word it picked, then searches with it. Your stick figure would search for "portrait figure". This is a rough stand-in, not real visual matching. True sketch search would need an image-recognition service.

5. search(). This is the core function. It builds one query from the text, the checked boxes and the year range, and always requires that an artwork has an image. It sends the query to the API, asking for only the id, title, artist and image id, 8 results per page. If the request fails, it shows a plain error message.

6. Showing results. Each artwork becomes a card with its image, title and artist. The image address is built from the artwork's image_id. The "~1,248" count in your sketch is the real total from the API. Pagination shows the previous page, the current page and its neighbours, "…", and the next page.

7. My Collection. The ♡ button on each card saves the artwork to your browser's local storage, so favorites survive a refresh. The My Collection tab shows those saved items without calling the API.

8. Wiring (bottom). This section connects the controls:

Clicking a tab switches views and hides the sketch pad when it isn't needed.
The top search box and Enter key run a text search.
Changing any filter re-runs the search from page 1.
Reset Filters clears everything.
One search() call at the end loads the first results when the page opens.



### Prompt 2

I need some further explanation of the code on how to achieve the function that users can draw the draft of the arts in this website

**AI's reply:**

Drawing works by combining four pieces: the canvas, pointer events, a coordinate conversion, and a small drawing loop. Here is each one with the code from the file.

1. The canvas is a blank pixel surface
html
<canvas id="cv" width="1000" height="180"></canvas>

A <canvas> is a rectangle of pixels that JavaScript can paint on. It has two sizes:

The width/height attributes (1000×180) set how many pixels the drawing has.
The CSS (width:100%; height:180px) sets how big it looks on screen.

They differ because the canvas stretches to fit the page. That is why step 3 has to convert coordinates.

js
const cv = $('#cv'), ctx = cv.getContext('2d');

ctx is the "paintbrush" object. Every drawing command goes through it.

The CSS touch-action: none on the canvas stops phones from scrolling the page while someone draws on it.

2. Pointer events tell us when and where the user draws

Three events make up a stroke:

js
cv.onpointerdown = e => { drawing = true; cv.setPointerCapture(e.pointerId); ctx.beginPath(); ctx.moveTo(...pos(e)); };
cv.onpointermove = e => { if (!drawing) return; ... };
cv.onpointerup   = () => drawing = false;
pointerdown fires when the mouse button is pressed or a finger or stylus touches. It sets the drawing flag, starts a new line with beginPath(), and puts the brush at the touch point with moveTo().
pointermove fires continuously as the pointer moves. If drawing is false (the mouse is just hovering), it does nothing.
pointerup fires on release and turns drawing off.

I used pointer events instead of mouse events because one set of handlers covers mouse, touch and stylus. setPointerCapture keeps the canvas receiving events even if the user's finger slides off the edge mid-stroke, so a stroke can't get stuck "on".

3. Converting screen position to canvas position
js
const pos = e => {
  const r = cv.getBoundingClientRect();
  return [(e.clientX - r.left) * cv.width / r.width,
          (e.clientY - r.top)  * cv.height / r.height];
};

The event gives the position on the browser window. The canvas needs a position in its own 1000×180 pixel grid. This does two things:

Subtracts the canvas's top-left corner (r.left, r.top) so the position is measured from the canvas's own corner.
Multiplies by the ratio of canvas pixels to displayed pixels (cv.width / r.width). On a small phone screen the canvas is displayed narrower than 1000px, so without this scaling the line would appear offset from your finger.
4. Drawing the line

Inside pointermove:

js
ctx.lineWidth = w; ctx.lineCap = 'round'; ctx.strokeStyle = '#1d2433';
ctx.lineTo(x, y);
ctx.stroke();

Each move event extends the line to the new point with lineTo, and stroke() paints it. The events fire many times per second, so many tiny straight segments join into what looks like a smooth curve. lineCap = 'round' rounds the line ends so the segments blend without gaps.

5. The tools (pen, eraser, clear, stroke size)

Eraser. Canvas has a drawing mode that removes pixels instead of adding them:

js
ctx.globalCompositeOperation = erasing ? 'destination-out' : 'source-over';
ctx.lineWidth = erasing ? w * 4 : w;

source-over is normal painting, and destination-out makes whatever you "paint" transparent. The eraser is also drawn 4× wider so it clears faster. The pen and eraser buttons only flip the erasing flag, and the on class highlights the active one.

Clear. ctx.clearRect(0, 0, cv.width, cv.height) wipes the whole canvas. The code also resets box to null so the app knows it's empty.

Stroke size. The variable w holds the width. − lowers it by 2 (never below 1), = resets it to 3, and + raises it by 2.

6. Remembering what was drawn

While the pen is moving, the code tracks the smallest rectangle around everything drawn:

js
box = box ? [Math.min(box[0],x), Math.min(box[1],y), Math.max(box[2],x), Math.max(box[3],y)] : [x,y,x,y];

box holds the left, top, right and bottom edges of the ink. "Use sketch to search" divides the box's height by its width to find out whether the drawing is tall, wide or squarish, and picks the search word from that. If box is still null, nothing has been drawn, so the app asks the user to draw first.

Current limits, and how to extend them
Erasing doesn't shrink the box. If you draw something wide and then erase it, the app still remembers the original size. A more accurate version would scan the canvas pixels with ctx.getImageData to measure the remaining ink.
The sketch isn't saved. It only lives on the canvas. To let users download it, you could add cv.toDataURL('image/png') and a download link.
No undo. Adding it means keeping a list of strokes and redrawing them all minus the last one.