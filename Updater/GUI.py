import pygtk
pygtk.require('2.0')
import gtk


class Prozor:
    def destroy(self, widget, data=None):
        gtk.main_quit()
    def __init__(self):
        self.prozor = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.prozor.show()
        self.prozor.connect("destroy", self.destroy)
        
    def main(self):
        gtk.main()
        
if __name__ == "__main__":
    base = Prozor()
    base.main()