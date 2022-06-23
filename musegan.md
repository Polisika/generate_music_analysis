# MuseGAN model
First vertical column defines state of the model, which generates the result.
Bigger digit means more trained model.

Here 1, 2 and 3 - is randomized vectors, that generates before the inference stage. 
Then they are goes to model's input as the state. 
So, models generates results from the same vectors. 
<table>
<tr><td>Num epochs</td><td>1</td><td>2</td><td>3</td></tr><tr>
    <td>5k</td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/5k/1.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/5k/2.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/5k/3.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
</tr>
<tr>
    <td>40k</td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/40k/1.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/40k/2.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/40k/3.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
</tr>
<tr>
    <td>100k</td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/100k/1.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/100k/2.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/100k/3.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
</tr>
<tr>
    <td>200k</td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/200k/1.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/200k/2.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/200k/3.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
</tr>
<tr>
    <td>1200k</td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/1200k/1.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/1200k/2.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="musegan/1200k/3.wav" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>
</tr>
</table>

## 5000 epochs genre definition of model results (MP3)
0-9 digits is genres definition.
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.0451</td>
      <td>0.0192</td>
      <td>0.0493</td>
      <td>0.1302</td>
      <td>0.1097</td>
      <td>0.0578</td>
      <td>0.0351</td>
      <td>0.2246</td>
      <td>0.0595</td>
      <td>0.2694</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0046</td>
      <td>0.0021</td>
      <td>0.0066</td>
      <td>0.0058</td>
      <td>0.0141</td>
      <td>0.0134</td>
      <td>0.0024</td>
      <td>0.0223</td>
      <td>0.0026</td>
      <td>0.0142</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.0417</td>
      <td>0.0177</td>
      <td>0.0452</td>
      <td>0.1198</td>
      <td>0.0611</td>
      <td>0.0499</td>
      <td>0.0270</td>
      <td>0.1640</td>
      <td>0.0527</td>
      <td style="color:red"><b>0.2553</b></td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.0430</td>
      <td>0.0180</td>
      <td>0.0452</td>
      <td>0.1277</td>
      <td>0.1066</td>
      <td>0.0505</td>
      <td>0.0336</td>
      <td>0.2040</td>
      <td>0.0582</td>
      <td>0.2620</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.0430</td>
      <td>0.0180</td>
      <td>0.0452</td>
      <td>0.1277</td>
      <td>0.1174</td>
      <td>0.0505</td>
      <td>0.0366</td>
      <td>0.2382</td>
      <td>0.0608</td>
      <td>0.2620</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.0464</td>
      <td>0.0214</td>
      <td>0.0561</td>
      <td>0.1299</td>
      <td>0.1180</td>
      <td>0.0649</td>
      <td>0.0366</td>
      <td>0.2382</td>
      <td>0.0608</td>
      <td>0.2661</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.0623</td>
      <td>0.0244</td>
      <td>0.0675</td>
      <td>0.1564</td>
      <td>0.1180</td>
      <td>0.1035</td>
      <td>0.0366</td>
      <td style="color:red"><b>0.2392</b></td>
      <td>0.0675</td>
      <td>0.3083</td>
    </tr>
  </tbody>
</table>

## 5000 epochs genre definition of model results (MIDI)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>genre</th>
      <th>Jazz</th>
      <th>Latin</th>
      <th>Country</th>
      <th>Electronic</th>
      <th>Pop_Rock</th>
      <th>Vocal</th>
      <th>New Age</th>
      <th>International</th>
      <th>RnB</th>
      <th>Rap</th>
      <th>Reggae</th>
      <th>Blues</th>
      <th>Folk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>73.0</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.0</td>
      <td>0.021</td>
      <td>0.023</td>
      <td>0.091</td>
      <td>0.052</td>
      <td>0.741</td>
      <td>0.002</td>
      <td>0.017</td>
      <td>0.006</td>
      <td>0.028</td>
      <td>0.007</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.001</td>
      <td>0.011</td>
      <td>0.017</td>
      <td>0.000</td>
      <td>0.002</td>
      <td>0.000</td>
      <td>0.003</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.001</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.0</td>
      <td>0.014</td>
      <td>0.018</td>
      <td>0.089</td>
      <td>0.028</td>
      <td>0.708</td>
      <td>0.002</td>
      <td>0.013</td>
      <td>0.006</td>
      <td>0.020</td>
      <td>0.006</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.0</td>
      <td>0.017</td>
      <td>0.021</td>
      <td>0.090</td>
      <td>0.043</td>
      <td>0.725</td>
      <td>0.002</td>
      <td>0.015</td>
      <td>0.006</td>
      <td>0.025</td>
      <td>0.006</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.0</td>
      <td>0.021</td>
      <td>0.023</td>
      <td>0.091</td>
      <td>0.050</td>
      <td>0.742</td>
      <td>0.002</td>
      <td>0.017</td>
      <td>0.006</td>
      <td>0.027</td>
      <td>0.007</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.0</td>
      <td>0.024</td>
      <td>0.025</td>
      <td>0.092</td>
      <td>0.062</td>
      <td>0.753</td>
      <td>0.002</td>
      <td>0.018</td>
      <td>0.006</td>
      <td>0.031</td>
      <td>0.007</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.0</td>
      <td>0.035</td>
      <td>0.027</td>
      <td>0.094</td>
      <td>0.076</td>
      <td>0.782</td>
      <td>0.002</td>
      <td>0.023</td>
      <td>0.007</td>
      <td>0.034</td>
      <td>0.008</td>
      <td>0.005</td>
      <td>0.004</td>
      <td>0.007</td>
    </tr>
  </tbody>
</table>

## 40000 epochs genre definition of model results (MP3)
0-9 is genres definition.
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
      <td>100.0000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.0573</td>
      <td>0.0240</td>
      <td>0.0655</td>
      <td>0.1461</td>
      <td>0.0639</td>
      <td>0.0909</td>
      <td>0.0282</td>
      <td>0.1778</td>
      <td>0.0540</td>
      <td>0.2924</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0083</td>
      <td>0.0041</td>
      <td>0.0101</td>
      <td>0.0074</td>
      <td>0.0149</td>
      <td>0.0221</td>
      <td>0.0033</td>
      <td>0.0107</td>
      <td>0.0024</td>
      <td>0.0251</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.0455</td>
      <td>0.0181</td>
      <td>0.0482</td>
      <td>0.1314</td>
      <td>0.0374</td>
      <td>0.0532</td>
      <td>0.0246</td>
      <td>0.1606</td>
      <td>0.0474</td>
      <td>0.2177</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.0480</td>
      <td>0.0217</td>
      <td>0.0566</td>
      <td>0.1410</td>
      <td>0.0523</td>
      <td>0.0712</td>
      <td>0.0256</td>
      <td>0.1729</td>
      <td>0.0524</td>
      <td>0.2943</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.0589</td>
      <td>0.0223</td>
      <td>0.0651</td>
      <td>0.1435</td>
      <td>0.0578</td>
      <td>0.0912</td>
      <td>0.0270</td>
      <td>0.1738</td>
      <td>0.0545</td>
      <td>0.3044</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.0622</td>
      <td>0.0242</td>
      <td>0.0669</td>
      <td>0.1467</td>
      <td>0.0798</td>
      <td>0.1032</td>
      <td>0.0321</td>
      <td>0.1814</td>
      <td>0.0555</td>
      <td>0.3076</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.0747</td>
      <td>0.0413</td>
      <td>0.0907</td>
      <td>0.1647</td>
      <td>0.1081</td>
      <td>0.1486</td>
      <td>0.0336</td>
      <td>0.2230</td>
      <td>0.0592</td>
      <td>0.3161</td>
    </tr>
  </tbody>
</table>

## 40000 epochs genre definition of model results (MIDI)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>genre</th>
      <th>Jazz</th>
      <th>Latin</th>
      <th>Country</th>
      <th>Electronic</th>
      <th>Pop_Rock</th>
      <th>Vocal</th>
      <th>New Age</th>
      <th>International</th>
      <th>RnB</th>
      <th>Rap</th>
      <th>Reggae</th>
      <th>Blues</th>
      <th>Folk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>73.0</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
      <td>73.000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.0</td>
      <td>0.021</td>
      <td>0.023</td>
      <td>0.091</td>
      <td>0.052</td>
      <td>0.741</td>
      <td>0.002</td>
      <td>0.017</td>
      <td>0.006</td>
      <td>0.028</td>
      <td>0.007</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.001</td>
      <td>0.011</td>
      <td>0.017</td>
      <td>0.000</td>
      <td>0.002</td>
      <td>0.000</td>
      <td>0.003</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.001</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.0</td>
      <td>0.014</td>
      <td>0.018</td>
      <td>0.089</td>
      <td>0.028</td>
      <td>0.708</td>
      <td>0.002</td>
      <td>0.013</td>
      <td>0.006</td>
      <td>0.020</td>
      <td>0.006</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.0</td>
      <td>0.017</td>
      <td>0.021</td>
      <td>0.090</td>
      <td>0.043</td>
      <td>0.725</td>
      <td>0.002</td>
      <td>0.015</td>
      <td>0.006</td>
      <td>0.025</td>
      <td>0.006</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.0</td>
      <td>0.021</td>
      <td>0.023</td>
      <td>0.091</td>
      <td>0.050</td>
      <td>0.742</td>
      <td>0.002</td>
      <td>0.017</td>
      <td>0.006</td>
      <td>0.027</td>
      <td>0.007</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.0</td>
      <td>0.024</td>
      <td>0.025</td>
      <td>0.092</td>
      <td>0.062</td>
      <td>0.753</td>
      <td>0.002</td>
      <td>0.018</td>
      <td>0.006</td>
      <td>0.031</td>
      <td>0.007</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.0</td>
      <td>0.035</td>
      <td>0.027</td>
      <td>0.094</td>
      <td>0.076</td>
      <td>0.782</td>
      <td>0.002</td>
      <td>0.023</td>
      <td>0.007</td>
      <td>0.034</td>
      <td>0.008</td>
      <td>0.005</td>
      <td>0.004</td>
      <td>0.007</td>
    </tr>
  </tbody>
</table>