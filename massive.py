from struct import *
import itertools

inputFile = "C:/Program Files/Native Instruments/massive/tables.dat"
outputDir = "C:/massive"
initialOffset=42
numWaves=384

outputtofile=True

class FileEntry:
  def __init__(self):
    self.dunno=0 # No idea what this field is for
    self.filenameLength=0
    self.fileName=""
    self.wavOffset=0
    self.wavLength=0

  def __repr__(self):
    return "dunno=%d, filenameLength=%d, fileName=%s, wavOffset=%d, wavLength=%d" \
        % (self.dunno, self.filenameLength, self.fileName, self.wavOffset, self.wavLength)

with open(inputFile, "rb") as f:
  nextSeek=42
  for _ in itertools.repeat(None, numWaves):
    f.seek(nextSeek)

    fileEntry = FileEntry()
    [fileEntry.dunno, fileEntry.filenameLength] = unpack('<ll', f.read(8))
    fileEntry.fileName = f.read(fileEntry.filenameLength);
    [fileEntry.wavOffset, fileEntry.wavLength] = unpack('<ll', f.read(8))

    nextSeek=f.tell()+1 # Null byte

    print fileEntry

    
    with open("%s/%d_%s" % (outputDir, fileEntry.wavOffset, fileEntry.fileName), "wb") as fo:
      f.seek(fileEntry.wavOffset)
      fo.write(f.read(fileEntry.wavLength))
