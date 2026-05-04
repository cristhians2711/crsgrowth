
(function(){
  const nav = document.getElementById('nav');
  const burger = document.getElementById('burger');
  const mob = document.getElementById('mob');
  const onScroll = () => {
    if(nav){ window.scrollY > 20 ? nav.classList.add('scrolled') : nav.classList.remove('scrolled'); }
  };
  window.addEventListener('scroll', onScroll, {passive:true});
  onScroll();

  window.toggleMob = function(){
    if(!burger || !mob) return;
    burger.classList.toggle('open');
    mob.classList.toggle('open');
    document.body.style.overflow = mob.classList.contains('open') ? 'hidden' : '';
  };
  window.closeMob = function(){
    if(!burger || !mob) return;
    burger.classList.remove('open');
    mob.classList.remove('open');
    document.body.style.overflow = '';
  };

  document.querySelectorAll('.rv').forEach(el=>{
    const obs = new IntersectionObserver(entries=>{
      entries.forEach(e=>{
        if(e.isIntersecting){ e.target.classList.add('in'); obs.unobserve(e.target); }
      });
    },{threshold:.12, rootMargin:'0px 0px -40px 0px'});
    obs.observe(el);
  });
})();
