import random, json


class JarManager():
    def __init__(self):
        
        with open("jar_holder.json", "r") as file:
            self.content = json.loads(file.read())
            self.keys = self.content["jar_keys"]
            
    def get_jar_keys(self):
        return self.content["jar_keys"]
    
    def get_jar(self, jar):
        return self.content[jar]
    
    def take_from_jar(self, jar):
        if not self.content[jar]:
            return None
        rdm = random.choice(self.content[jar])
        self.remove_entry(jar, rdm)
        return rdm
    
    def add_jar(self, jarname, jar=list):
        self.keys.append(jarname)
        self.content[jarname] = jar
        
    def remove_jar(self, jarname):
        self.keys.remove(jarname)
        self.content.pop(jarname)
        
    def add_entry(self, jarname, value):
        self.content[jarname].append(value)
        
    def remove_entry(self, jar, entry):
        self.content[jar].remove(entry)
        
    def write_file(self):
        with open("jar_holder.json", "w") as file:
            file.write(json.dumps(self.content))