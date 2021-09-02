import time

class Inverter():

    def __init__(self, name, port):
      self.name= name
      self.port= port
      self.dev= open(self.port, 'rb+')

    def query(self, command):

      retVal= []
      done = False
      try:
        self.dev= open(self.port, 'rb+')
      
      except:
        print(self.port, 'not connected')
        return retVal

      if (self.dev):
        try:
          self.dev.write(command)

          while not done:

            buffer  = self.dev.read(8)
            for c in buffer:
              #look for \r
                retVal.append(c)
                #print(c)
                if(c== 13):
                  done= True

          self.dev.close()

            #retVal= data #str(data).split('(')[1].split(' ')
            #print('id: ', id(self.dev), 'len: ', len(data))

        except Exception as e:
          print("Error:", e)
      
      else:
        retVal= None

      return bytes(retVal)


    def Connect(self, port):
      self.dev= open(port, 'rb+')
