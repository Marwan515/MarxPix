<h2> This Project Was For The CS50 Final Project</h2>
<p>MarXPiX is A Website</p>
<p>On This Website You'll Be Able To Generate Image From One Of Nasa's Mars Rover's</p>
<p>This Project Utilizes <a href="https://api.nasa.gov">Nasa's Open API</a></p>
<hr>
<section>
    <h3>The Homepage Has 2 Sections</h3>
    <h4>1st Section Utilizes Nasa's open Api Of APOD</h4>
    <p>Example: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY</p>
    <p>Which Provides Us With Astronomy Picture Of The Day</p>
    <p>Each Day It Generates a New Picture</p>
    <h4>2nd Section Utilizes Nasa's Open Api Of Mars Rover Photos</h4>
    <p>First We Use https://api.nasa.gov/mars-photos/api/v1/manifests/curiosity/?api_key=DEMO_KEY To Get Rover Data</p>
    <p>Then I Check The Rover's Data if Rover is Active Then We Update The Rover's Data Else Skip</p>
</section>
<section>
    <h3>The Image Generating Page</h3>
    <p>This Page Has A Form With two Drop Down options The Defaults Will Generate The Latest Images With Any Camera</p>
    <p>If You Select The Earth Date Then You'll Only Be Able To Use The Date Input And Vice Versa</p>
    <p>You Can Select Any Camera From The Options And Generate</p>
</section>
<section>
    <h3>The Generated Image Pages</h3>
    <p>This Page Shows The Rover Date And Images</p>
    <p>The Images Has The Name Of The Camera And Date's It Was Captured</p>
    <p>Images Are Clickable And It Will Redirect You To The Link That The Api Provided</p>
</section>
<hr>
MIT License

Copyright (c) 2022 Marwan Abdulmannan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
