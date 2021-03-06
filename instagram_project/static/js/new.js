<div class="card mb-3 ">
        <div class="row g-0">
          <div class="col-md-8">
            <img src="{{detail.picture.url}}" class="" alt="..." style="width:530px; min-height:350px;height:{{detail.picture.height}}px;">
          </div>
          <div class="col-md-4">
            <div class="card-body h">
              <div class="row lk">
                <div class="col-md-10 nopa">
                  <p class="m">
                    <a href='{% url "insta:user_profile" pk=detail.author.pk %}'>
                      {% if detail.author.display_picture|check %}
                        <img class="adjust" src="{{detail.author.display_picture.url}}" alt="">
                      {% endif %}
                    </a>

                    <span class="lefte st">{{detail.author}}</span>
                    {% if detail.author in user.following.all %}
                    <button type="button" class="btn btn-sm buto" name="button"><span class="w"><a href="">Following</a></span></button>
                    {% else %}
                      <button type="button" class="btn-md btn c t" name="button"><span class="w"><a href="{% url "insta:follow" pk=detail.pk %}">Follow</a></span></button>
                    {% endif %}

                  </p>
                </div>
                <!-- <div class="col-md-2 align">
                  <span class="yo">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
                      <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
                    </svg>
                  </span>

                </div> -->
                <hr class="po">

              </div>

              <!-- <div class="row sd " style=''>
                <div class="row td">
                  <div class="col-md-2 ">
                    <img class="round" src="{{detail.author.display_picture.url}}" alt="">
                  </div>
                  <div class="col-md-10 ">
                    <p class="card-text"> <span class="lefte st">{{detail.author}}-</span> <span class="st">{{detail.text}}</span></p>

                  </div>
                </div>
                {% for comment in comments %}
                <div class="row td">
                  <div class="col-md-2 ">
                    <img class="round" src="{{comment.author.display_picture.url}}" alt="">
                  </div>
                  <div class="col-md-10 ">
                    <p class="card-text"> <span class="lefte st">{{comment.author}}</span> <span class="st">{{comment.text}}</span></p>

                  </div>
                </div>
                {% endfor %}
              </div> -->

              <!-- <hr> -->
              <ul class="flex">
                <li>
                    {% if likes %}
                    <a class="nav-link active leftpad like " aria-current="page" href="{% url "insta:unlike" pk=detail.pk %}">
                      <svg  xmlns="http://www.w3.org/2000/svg" width="29" height="24" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                      </svg>
                    </a>
                    {% else %}
                    <a class="nav-link active leftpad" aria-current="page" href="{% url "insta:like" pk=detail.pk %}">
                      <svg  xmlns="http://www.w3.org/2000/svg" width="29" height="24" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                      </svg>
                    </a>

                    {% endif %}
                </li>
                <li>
                  <a class="nav-link active leftpad" aria-current="page" href="{% url "insta:detail" pk=detail.pk %}">
                    <svg xmlns="http://www.w3.org/2000/svg" width="29" height="24" fill="currentColor" class="bi bi-chat" viewBox="0 0 16 16">
                      <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"/>
                    </svg>
                  </a>
                </li>
                <li>
                  <a class="nav-link active leftpad" aria-current="page" href="#">
                    <svg xmlns="http://www.w3.org/2000/svg" width="29" height="24" fill="currentColor" class="bi bi-telegram" viewBox="0 0 16 16">
                      <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z"/>
                    </svg>
                  </a>
                </li>
                <li>
                {% if detail in user.saved.all %}
                <a class="nav-link active leftpad saved le" aria-current="page" href="{% url "insta:unsave" pk=detail.pk %}">
                {% else %}
                <a class="nav-link active leftpad le" aria-current="page" href="{% url "insta:save" pk=detail.pk %}">
                {% endif %}
                    <svg xmlns="http://www.w3.org/2000/svg" width="29" height="24" fill="currentColor" class="bi bi-bookmark" viewBox="0 0 16 16">
                      <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
                    </svg>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>