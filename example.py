import sys
from qtpy import QtCore, QtWidgets
import qtawesome as qta
from six import unichr


class AwesomeExample(QtWidgets.QDialog):

    def __init__(self):
        super(AwesomeExample, self).__init__()

        # Get icons by name.
        fa_icon = qta.icon('fa.flag')
        fa_button = QtWidgets.QPushButton(fa_icon, 'Font Awesome!')

        asl_icon = qta.icon('ei.asl')
        elusive_button = QtWidgets.QPushButton(asl_icon, 'Elusive Icons!')

        # Styling
        styling_icon = qta.icon('fa.music',
                                active='fa.legal',
                                color='blue',
                                color_active='orange')
        music_button = QtWidgets.QPushButton(styling_icon, 'Styling')

        # Render a label with this font
        label = QtWidgets.QLabel(unichr(0xf19c) + ' ' + 'Label')
        label.setFont(qta.font('fa', 16))

        # Stack icons
        camera_ban = qta.icon('fa.camera', 'fa.ban',
                              options=[{'scale_factor': 0.5,
                                        'active': 'fa.legal'},
                                       {'color': 'red', 'opacity': 0.7}])
        stack_button = QtWidgets.QPushButton(camera_ban, 'Stack')
        stack_button.setIconSize(QtCore.QSize(32, 32))

        # Spin icons
        spin_button = QtWidgets.QPushButton(' Spinning icon')
        spin_icon = qta.icon('fa.spinner', color='red',
                             animation=qta.Spin(spin_button))
        spin_button.setIcon(spin_icon)

        # Pulse icons
        pulse_button = QtWidgets.QPushButton(' Pulsing icon')
        pulse_icon = qta.icon('fa.spinner', color='green',
                              animation=qta.Pulse(pulse_button))
        pulse_button.setIcon(pulse_icon)

        # Stacked spin icons
        stack_spin_button = QtWidgets.QPushButton('Stack spin')
        options = [{'scale_factor': 0.4,
                    'animation': qta.Spin(stack_spin_button)},
                   {'color': 'blue'}]
        stack_spin_icon = qta.icon('ei.asl', 'fa.square-o',
                                   options=options)
        stack_spin_button.setIcon(stack_spin_icon)
        stack_spin_button.setIconSize(QtCore.QSize(32, 32))
        # Stack and offset icons
        saveall = qta.icon('fa.save', 'fa.save',
                           options=[{'scale_factor': 0.8,
                                     'offset': (0.2, 0.2),
                                     'color': 'gray'},
                                    {'scale_factor': 0.8}])
        saveall_button = QtWidgets.QPushButton(saveall, 'Stack, offset')

        # Layout
        vbox = QtWidgets.QVBoxLayout()
        widgets = [fa_button, elusive_button, music_button, stack_button,
                   saveall_button, spin_button, pulse_button,
                   stack_spin_button, label]
        for w in widgets:
            vbox.addWidget(w)

        self.setLayout(vbox)
        self.setWindowTitle('Awesome')
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    # Enable High DPI display with PyQt5
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtCore.QTimer.singleShot(5000, app.exit)
    _ = AwesomeExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
