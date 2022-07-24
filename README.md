# pubmed-api
An api built to pubmed rct dataset to classify medical abstract into Background ,Objective, method, results, conclusion based on a custom built Tensorflow2.x deep Model
<h3>API CALL link : https://pubmed-api-test.herokuapp.com/</h3>
<h2>DOCS:</h2>
<p>
<b>opensourced for any user to call no api-key required</b><br>
<h4> link to Model developement notebook repo: https://github.com/average-joe25/scientific-abstract-classifier</h4>
<h5>To get abstract classified</h5>
request:<br>

method: GET<br>
type: application/json<br>
body: {data: string}<br>

response:<br>
type: application/json<br>
body: {value: string}<br>
</p>
<h4>Example</h4>
<img src="https://github.com/average-joe25/attached-imgs-repo/blob/main/Screenshot%202022-07-24%20153520.png?raw=true">
