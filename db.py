import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name text, age INTEGER, p1class text, p1teacher text, p2class text, p2teacher text, p3class text, p3teacher text, p4class text, p4teacher text, p5class text, p5teacher text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, age, p1class, p1teacher, p2class, p2teacher, p3class, p3teacher, p4class, p4teacher, p5class, p5teacher):
        self.cur.execute("INSERT INTO students VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (name, age, p1class, p1teacher, p2class, p2teacher, p3class, p3teacher, p4class, p4teacher, p5class, p5teacher))
        self.conn.commit()
        print("student added")

    def remove(self, id):
        self.cur.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, age, p1class, p1teacher, p2class, p2teacher, p3class, p3teacher, p4class, p4teacher, p5class, p5teacher):
        self.cur.execute("UPDATE students SET name = ?, age = ?, p1class = ?, p1teacher = ?, p2class = ?, p2teacher = ?, p3class = ?, p3teacher = ?, p4class = ?, p4teacher = ?, p5class = ?, p5teacher = ? WHERE id = ?",
                         (name, age, p1class, p1teacher, p2class, p2teacher, p3class, p3teacher, p4class, p4teacher, p5class, p5teacher, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('store.db')
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")