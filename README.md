# Solfeggietto
Classic by Carl Philipp Emanuel Bach transcribed to a python script to output TAB for guitar

Because the song is almost entirely 16th notes, I have transcribed it with no timing informaiton.
Where chords are played (and sustained) I only include the root note and repeat it several times.
Each note is encoded as 3 characters indicating note and octave. The key signature is included separately
but individual notes can be forced flat (b) sharp(#) or natural (n) with the 3rd character.

The text-encoded notes are converted to their MIDI values, an offset is added to transpose, and each note
is printed in the TAB in every position it can be played on the guitar. This leaves it to the player to
select what fingering to use. I like to use a highlighter on a printout to choose my way. There is also
an ability to limit how high up the neck you want to go per-string and alternate tunings are supported.

The output file was done in standard tuning with everything shifted down one half step. This helps to fit
all of the notes an a 22 fret guitar while also making the lowest note an open low E, which you may need since it
directly follows fret 20 on the B string... Yes this piece is a wild ride ;-)
