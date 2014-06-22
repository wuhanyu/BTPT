class HomeController < ApplicationController
  layout "homelayout", except: [:login]
  def index
    @zone = 'index'
  end
  
  def fileupload
    @zone = 'fileupload'
  end
  
  def mbfunction
    @zone = 'mbfunction'
  end
  
  def frulecal
    @zone = 'frulecal'
  end
  
  def fruleview
    @zone = 'fruleview'
  end
  
  def login
  end

  def apply
    
  end
  
  def admission
     
  end
  
end