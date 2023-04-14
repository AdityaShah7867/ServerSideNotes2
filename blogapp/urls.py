from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home,name='home'),

    # User action routes for added notes starts here
    path('addNotes/', views.addNotes,name='addNotes'),
    path('status/',views.status,name='status'),
    path('status/<slug:slug>/',views.noteDelete,name='noteDelete'),
    # User action routes for added notes ends here



    # Notes Routing starts here

    path('notes/', views.notes,name='notes'),
    path('lectslides/',views.lectslides,name='lectSlides'),
    path('referenceBooks/',views.refeBk,name='referenceBooks'),
    path('pyq/',views.pyqA,name='pyqA'),
    path('Assignment/',views.Assignment,name='Assignment'),

    # Note viewer routes starts here
    path('notes/<slug:slug>/',views.noteViewer,name='notesViewer'),
    path('like/<int:pk>/', views.like_notes, name='like_notes'),
    path('buy/<int:pk>/', views.buy_notes, name='buy_notes'),
    path('notes/<slug:slug>/comment/',views.cmntAll,name='cmntAll'),
    path('notes/<slug:slug>/comment/<slug:slugA>/',views.replyA,name='replyA'),
    path('seeRply/<slug:slug>/',views.seeRply,name='seeRply'),
    # Note viewer routes ends here

    # Notes Routing ends here



    # User authentication starts here
    path('login/', views.loginR,name='loginR'),
    path('logout/',views.logoutR,name='logout'),
    path('register/',views.registerR,name='register'),
    path('activate-user/<uidb64>/<token>/',views.activate_user,name='activate'),
    # User authentication ends here


    
    # Admin panel routing starts here
    path('adminResponse/',views.adminResponse,name='adminResponse'),
    path('addDriveLink/<slug:slug>/',views.addDriveLink,name='addDriveLink'),
    path('adminResponse/<slug:slug>/',views.upDelete,name='upDelete'),
    path('acceptStatus/<slug:slug>/',views.acceptStatus,name='acceptStatus'),
    # Admin panel routing ends here

    # Dashboard routing starts here
    path('dashboard/', views.dashboard,name='dashboard'),
    path('notesuploded/',views.notesuploded,name='notesuploded'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path('noteslikes', views.notes_likes, name='noteslikes'),
    path('notesbought/', views.notesbought, name='notesbought'),
    path('bookmark/', views.bookmark, name='bookmark'),
    # Dashboard routing ends here
    
    
    

    # Extra content routes starts here 
    path('searchNotes/',views.searchNotes,name='searchNotes'),
    path('searchRecmd/',views.searchRecmd,name='searchRecmd'),
    path('aboutus/',views.aboutUs,name='about'),
    path('faculty/',views.teacher,name='teacher'),
    path('add_reminder/', views.add_reminder, name='add_reminder'),
    path('reminder_list/', views.reminder_list, name='reminder_list'),
    # Extra content routes ends here 

]