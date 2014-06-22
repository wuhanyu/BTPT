class HomeController < ApplicationController
  layout "homelayout", except: [:login]
  def index
    @zone = 'index'
  end
  
  def fileupload
    @zone = 'fileupload'
  end
  
  def login
  end

  def apply
    
  end
  
  def admission
     
  end
  
end